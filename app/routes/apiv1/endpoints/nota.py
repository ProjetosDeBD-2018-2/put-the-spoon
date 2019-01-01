from sqlalchemy.sql import func

from flask_restplus import Namespace, Resource

from app.schemas.nota import Nota
from app.schemas.nota import AverageRatingsByRegion
from app.schemas.endereco import Endereco

from app.routes.apiv1.serializers import nota_model
from app.routes.apiv1.serializers import values_by_region

nota = Namespace('Notas')


@nota.route('/getAll')
class GetAllNotas(Resource):
    @nota.marshal_list_with(nota_model)
    def get(self):
        result = Nota.query.all()
        return result


@nota.route('/AverageByRegion/<int:year>')
class AverageRegion(Resource):
    @nota.marshal_list_with(values_by_region)
    def get(self, year):
        result = \
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
        output = serialized_schema.dump(result).data
        return output
