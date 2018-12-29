from app.extensions import ma

from .ies import Ies


class IesSerializedSchema(ma.ModelSchema):
    class Meta:
        model = Ies
