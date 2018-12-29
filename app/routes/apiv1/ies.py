from flask import jsonify
from flask_restplus import Namespace, Resource

from app.schemas.ies import Ies
from app.schemas.serializers import IesSerializedSchema

ies = Namespace('Users')


@ies.route('/')
class AllIes(Resource):
    def get(self):
        ies = Ies.query.all()
        serialized_schema = IesSerializedSchema(many=True)
        output = serialized_schema.dump(ies).data
        return jsonify(output)


@ies.route('/<int:cod_ies>')
class SingleIes(Resource):
    def get(self, cod_ies):
        ies = Ies.query.get(cod_ies)
        serialized_schema = IesSerializedSchema()
        output = serialized_schema.dump(ies).data
        return jsonify(output)
