from flask import jsonify
from sqlalchemy.sql import func
from flask_restplus import Namespace, Resource

from app.schemas.ies import Ies
from app.schemas.despesas import Despesas
from app.schemas.rubrica import Rubrica
from app.schemas.orcamento import Orcamento

from app.schemas.serializers import OrcamentoSerialized

orcamento = Namespace('Orcamento')


@orcamento.route('/getAll')
class GetAllOrcamento(Resource):
    def get(self):
        notas = Orcamento.query.all()
        serialized_schema = OrcamentoSerialized(many=True)
        output = serialized_schema.dump(notas).data
        return jsonify(output)


@orcamento.route('/HighestExpenseByType/<int:year>/<int:typex>')
class HighestExpenseByType(Resource):
    def get(self, year):
        subquery = Orcamento.query.with_entities(
            Despesas.idIes,
            func.sum(Orcamento.orcamento_atualizado).label('orcamento'),
            func.sum(Rubrica.valor_pago_reais).label('despesaTotal')
        ).filter(
            Orcamento.exercicio == year,
            Despesas.ano_mes_lancamento.like(f"{year}%"),
            Orcamento.codigo_orgao_subordinado == Despesas.codigo_orgao_subordinado,
            Despesas.idRubrica == Rubrica.id
        ).group_by(
            Despesas.idIes
        ).all()

        result = 

        result = None

        serialized_schema = IesHighestExpenseByType(many=True)
        output = serialized_schema.dump(result).data
        return jsonify(output)
