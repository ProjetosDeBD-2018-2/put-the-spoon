from flask import Blueprint
from flask_restplus import Api

from .ies import ies
from .nota import nota
from .despesas import despesas

api_v1 = Blueprint('api', __name__, url_prefix='/api/1')

api = Api(api_v1,
          title='My Title',
          version='1.0',
          description='A description',
          )

api.add_namespace(ies)
api.add_namespace(nota)
api.add_namespace(despesas)
