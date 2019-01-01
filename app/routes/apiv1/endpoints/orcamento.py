from sqlalchemy.sql import func
from flask_restplus import Namespace, Resource

from app.schemas.orcamento import Orcamento
from app.schemas.orcamento import HighestExpenseByTypeDespesa
from app.schemas.ies import Ies
from app.schemas.despesas import Despesas
from app.schemas.rubrica import Rubrica

from app.routes.apiv1.serializers import highest_expense_by_type

orcamento = Namespace('Orcamento')


@orcamento.route('/HighestExpenseByType/<int:year>/<string:order>')
class HighestExpenseByType(Resource):
    @orcamento.marshal_list_with(highest_expense_by_type)
    @orcamento.doc(responses={400: 'Invalid input'})
    def get(self, year, order):
        subquery = \
            Orcamento.query.with_entities(
                Despesas.idIes,
                func.sum(Orcamento.orcamento_atualizado).label('orcamento'),
                func.sum(Rubrica.valor_pago_reais).label('total')
            ).filter(
                Orcamento.exercicio == year,
                Despesas.ano_mes_lancamento.like(f"{year}%"),
                Orcamento.codigo_orgao_subordinado == Despesas.codigo_orgao_subordinado,
                Despesas.idRubrica == Rubrica.id
            ).group_by(
                Despesas.idIes
            ).subquery('subquery')

        query = \
            Ies.query.with_entities(
                subquery.columns.idIes,
                Ies.nome_ies,
                subquery.columns.orcamento,
                subquery.columns.total
            )

        if (order == 'greater'):
            query = query.filter(
                subquery.columns.idIes == Ies.cod_ies,
                subquery.columns.total > subquery.columns.orcamento
            )
        elif (order == 'smaller'):
            result = query.filter(
                subquery.columns.idIes == Ies.cod_ies,
                subquery.columns.total < subquery.columns.orcamento
            )
        else:
            return orcamento.abort(400)

        result = query.all()
        serialized_schema = HighestExpenseByTypeDespesa(many=True)
        output = serialized_schema.dump(result).data
        return output
