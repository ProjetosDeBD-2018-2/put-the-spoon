from app.extensions import ma

from .ies import Ies
from .nota import Nota


class IesSerialized(ma.ModelSchema):
    class Meta:
        model = Ies


class NotaSerialized(ma.ModelSchema):
    class Meta:
        model = Nota


class AverageRatingsByRegion(ma.Schema):
    class Meta:
        fields = ('regiaoIes', 'total')


class RegionsWithExpenses(ma.Schema):
    class Meta:
        fields = ('regiaoIes', 'DespesaTotal')


class RelationshipBetweenExpensesAndRatings(ma.Schema):
    class Meta:
        fields = (
            'idIes', 'nome_ies', 'idNota',
            'igcContinuo', 'idTipoDespesa',
            'tipo_despesa', 'DespesaTotal'
        )


class IesHighestExpenseByType(ma.Schema):
    class Meta:
        fields = ('idTipoDespesa', 'idIes', 'maximo')


class IesLowestExpenseByType(ma.Schema):
    class Meta:
        fields = ('idTipoDespesa', 'idIes', 'minimo')
