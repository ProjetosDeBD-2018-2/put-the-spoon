from flask import Blueprint
from flask_restplus import Api

from .endpoints.ies import ies
from .endpoints.nota import nota
from .endpoints.despesas import despesas

from .serializers import ies_model
from .serializers import expense_by_type
from .serializers import expenses_and_ratings
from .serializers import nota_model
from .serializers import values_by_region

api_v1 = Blueprint('api', __name__, url_prefix='/api/1')

api = Api(api_v1,
          title='My Title',
          version='1.0',
          description='A description',
          )

api.add_namespace(ies)
api.add_namespace(nota)
api.add_namespace(despesas)

api.models[ies_model.name] = ies_model
api.models[expense_by_type.name] = expense_by_type
api.models[expenses_and_ratings.name] = expenses_and_ratings
api.models[nota_model.name] = nota_model
api.models[values_by_region.name] = values_by_region
