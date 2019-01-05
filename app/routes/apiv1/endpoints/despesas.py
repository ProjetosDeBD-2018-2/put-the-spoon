from sqlalchemy.sql import func

from flask_restplus import Namespace, Resource

from app.schemas.despesas import Despesas
from app.schemas.despesas import RegionsWithExpenses
from app.schemas.rubrica import Rubrica
from app.schemas.endereco import Endereco

from app.routes.apiv1.serializers import values_by_region

despesas = Namespace('Despesa')


@despesas.route('/ExpensesByRegions/<int:year>')
class ExpensesByRegions(Resource):
    @despesas.marshal_list_with(values_by_region)
    def get(self, year):
        notas = \
            Despesas.query.with_entities(
                Endereco.regiaoIes,
                func.sum(Rubrica.valor_pago_reais).label('despesa')
            ).filter(
                Despesas.id == Rubrica.id_despesa,
                Despesas.ano_mes_lancamento.like(f"{year}%"),
                Endereco.cod_ies == Despesas.idIes
            ).group_by(
                Endereco.regiaoIes
            ).all()

        serialized_schema = RegionsWithExpenses(many=True)
        output = serialized_schema.dump(notas).data
        return output
