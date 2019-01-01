from flask import jsonify
from sqlalchemy.sql import func
from flask_restplus import Namespace, Resource

from app.schemas.ies import Ies
from app.schemas.nota import Nota
from app.schemas.despesas import Despesas
from app.schemas.tipoDespesa import TipoDespesa
from app.schemas.rubrica import Rubrica

from app.schemas.serializers import IesSerialized
from app.schemas.serializers import IesExpenseByType
from app.schemas.serializers import RelationshipBetweenExpensesAndRatings

ies = Namespace('Ies')


@ies.route('/<int:cod_ies>')
class Default(Resource):
    def get(self, cod_ies):
        result = Ies.query.get(cod_ies)
        serialized_schema = IesSerialized()
        output = serialized_schema.dump(result).data
        return jsonify(output)


@ies.route('/getAll')
class GetAllIes(Resource):
    def get(self):
        result = Ies.query.all()
        serialized_schema = IesSerialized(many=True)
        output = serialized_schema.dump(result).data
        return jsonify(output)


@ies.route('/RelationshipExpensesAndRatings/<int:year>')
class RelationshipExpensesAndRatings(Resource):
    def get(self, year):
        result = Ies.query.with_entities(
            Nota.idIes,
            Ies.nome_ies,
            Nota.idNota,
            Nota.igcContinuo,
            Despesas.idTipoDespesa,
            TipoDespesa.tipo_despesa,
            func.avg(Rubrica.valor_pago_reais).label('DespesaTotal')
        ).filter(
            Despesas.id == Rubrica.id_despesa,
            Despesas.idIes == Nota.idIes,
            Nota.idIes == Ies.cod_ies,
            TipoDespesa.id == Despesas.idTipoDespesa,
            Nota.anoNota == year,
            Despesas.ano_mes_lancamento.like(f"{year}%")
        ).group_by(
            Nota.idIes,
            Ies.nome_ies,
            Nota.idNota,
            Nota.igcContinuo,
            Despesas.idTipoDespesa,
            TipoDespesa.tipo_despesa
        ).all()

        serialized_schema = RelationshipBetweenExpensesAndRatings(many=True)
        output = serialized_schema.dump(result).data
        return jsonify(output)


@ies.route('/ExpenseByType/<int:year>/<int:typex>/<string:order>')
class ExpenseByType(Resource):
    def get(self, year, typex, order):
        query = Ies.query.with_entities(
            Despesas.idTipoDespesa,
            Despesas.idIes,
            func.sum(Rubrica.valor_pago_reais).label('total')
        ).filter(
            Despesas.id == Rubrica.id_despesa,
            Despesas.idTipoDespesa == TipoDespesa.id,
            Despesas.idTipoDespesa == typex,
            Despesas.ano_mes_lancamento.like(f"{year}%")
        ).group_by(
            Despesas.idTipoDespesa,
            Despesas.idIes
        )

        if (order == 'desc'):
            query = query.order_by(func.sum(Rubrica.valor_pago_reais).desc())
        elif (order == 'asc'):
            query = query.order_by(func.sum(Rubrica.valor_pago_reais).asc())
        else:
            return ies.abort(400, 'Order type not valid')

        result = query.all()
        serialized_schema = IesExpenseByType(many=True)
        output = serialized_schema.dump(result).data
        return jsonify(output)
