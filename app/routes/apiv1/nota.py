from flask import jsonify
from sqlalchemy.sql import func

from flask_restplus import Namespace, Resource

from app.schemas.nota import Nota
from app.schemas.endereco import Endereco

from app.schemas.serializers import NotaSerialized
from app.schemas.serializers import AverageRatingsByRegion

nota = Namespace('Notas')


@nota.route('/getAll')
class GetAllNotas(Resource):
    def get(self):
        notas = Nota.query.all()
        serialized_schema = NotaSerialized(many=True)
        output = serialized_schema.dump(notas).data
        return jsonify(output)


@nota.route('/AverageByRegion/<int:year>')
class AverageRegion(Resource):
    def get(self, year):
        notas = \
            Nota.query.with_entities(
                Endereco.regiaoIes,
                func.avg(Nota.igcContinuo).label('total')
            ).filter(
                Nota.idIes == Endereco.cod_ies,
                Nota.anoNota == year
            ).group_by(
                Endereco.regiaoIes
            ).all()

        serialized_schema = AverageRatingsByRegion(many=True)
        output = serialized_schema.dump(notas).data
        return jsonify(output)
