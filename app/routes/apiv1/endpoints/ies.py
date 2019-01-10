from sqlalchemy.sql import func
from flask_restplus import Namespace, Resource

from app.schemas.ies import Ies
from app.schemas.ies import ExpenseByTypeSchema
from app.schemas.ies import ExpensesAndRatingsSchema

from app.schemas.nota import Nota
from app.schemas.despesas import Despesas
from app.schemas.tipoDespesa import TipoDespesa
from app.schemas.rubrica import Rubrica

from app.routes.apiv1.serializers import ies_model
from app.routes.apiv1.serializers import expense_by_type
from app.routes.apiv1.serializers import expenses_and_ratings

ies = Namespace('Ies')


@ies.route('/<int:cod_ies>')
class Default(Resource):
    @ies.marshal_with(ies_model)
    def get(self, cod_ies):
        result = Ies.query.get(cod_ies)
        return result


@ies.route('/getAll')
class GetAllIes(Resource):
    @ies.marshal_list_with(ies_model)
    def get(self):
        result = Ies.query.all()
        return result


@ies.route('/RelationshipExpensesAndRatings/<int:year>/<string:order>')
class RelationshipExpensesAndRatings(Resource):
    @ies.marshal_list_with(expenses_and_ratings)
    def get(self, year, order):
        query = \
            Ies.query.with_entities(
                Ies.nome_ies,
                Nota.igcContinuo,
                func.sum(Rubrica.valor_pago_reais).label('DespesaTotal')
            ).filter(
                Despesas.id == Rubrica.id_despesa,
                Despesas.idIes == Nota.idIes,
                Nota.idIes == Ies.cod_ies,
                Nota.anoNota == year,
                Despesas.ano_mes_lancamento.like(f"{year}%")
            ).group_by(
                Ies.nome_ies,
                Nota.igcContinuo,
            )

        if (order == 'desc'):
            query = query.order_by(Nota.igcContinuo).desc()
        elif (order == 'asc'):
            query = query.order_by(Nota.igcContinuo).asc()
        else:
            return ies.abort(400)

        result = query.all()
        serialized_schema = ExpensesAndRatingsSchema(many=True)
        output = serialized_schema.dump(result).data
        return output

"""
@ies.route('/Expense/<int:year>/<int:typex>/<string:order>')
class ExpenseBy(Resource):
    def get(self, year, typex, order):
        subquery = \
            Despesas.query.with_entities(
                Despesas.idTipoDespesa,
                TipoDespesa.tipo_despesa,
                Despesas.idIes,
                func.sum(Rubrica.valor_pago_reais).label('despesa_total')
            ).filter(
                Despesas.id == Rubrica.id_despesa,
                Despesas.idTipoDespesa == TipoDespesa.id,
                Despesas.idTipoDespesa == typex,
                Despesas.ano_mes_lancamento.like(f"{year}%")
            ).group_by(
                Despesas.idIes,
                Despesas.idIes
            )

        if (order == 'desc'):
            query = \
                subquery.order_by(
                    func.sum(Rubrica.valor_pago_reais
                ).desc()).subquery('subquery')
        elif (order == 'asc'):
            query = \
                subquery.order_by(
                    func.sum(Rubrica.valor_pago_reais
                ).asc()).subquery('subquery')
        else:
            return ies.abort(400)

        query = \
            Ies.query.with_entities(
                subquery.columns.idTipoDespesa,
                subquery.columns.tipo_despesa,
                Ies.nome_ies,
                Ies.sigla_ies,
                subquery.columns.despesa_total
            ).filter(
                subquery.columns.idIes == 
            )

        result = query.all()
        serialized_schema = HighestExpenseByTypeDespesa(many=True)
        output = serialized_schema.dump(result).data
        return output
"""

@ies.route('/ExpenseByType/<int:year>/<int:typex>/<string:order>')
class ExpenseByType(Resource):
    @ies.marshal_list_with(expense_by_type)
    @ies.doc(responses={400: 'Invalid input'})
    def get(self, year, typex, order):
        query = \
            Ies.query.with_entities(
                Ies.nome_ies,
                Despesas.idTipoDespesa,
                TipoDespesa.tipo_despesa,
                Despesas.idIes,
                func.sum(Rubrica.valor_pago_reais).label('despesa')
            ).filter(
                Despesas.id == Rubrica.id_despesa,
                Despesas.idTipoDespesa == TipoDespesa.id,
                Despesas.idTipoDespesa == typex,
                Despesas.ano_mes_lancamento.like(f"{year}%")
            ).group_by(
                Ies.nome_ies,
                Despesas.idTipoDespesa,
                Despesas.idIes,
                TipoDespesa.tipo_despesa
            )

        if (order == 'desc'):
            query = query.order_by(func.sum(Rubrica.valor_pago_reais).desc())
        elif (order == 'asc'):
            query = query.order_by(func.sum(Rubrica.valor_pago_reais).asc())
        else:
            return ies.abort(400)

        result = query.all()
        serialized_schema = ExpenseByTypeSchema(many=True)
        output = serialized_schema.dump(result).data
        return output
