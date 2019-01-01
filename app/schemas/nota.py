from app.extensions import db
from app.extensions import ma


class Nota(db.Model):
    __tablename__ = 'Nota'
    idNota = db.Column(db.INT(), primary_key=True)
    anoNota = db.Column(db.INT())
    idIes = db.Column(db.INT())
    igcContinuo = db.Column(db.NVARCHAR(500))
    igcFaixa = db.Column(db.NVARCHAR(500))


class AverageRatingsByRegion(ma.Schema):
    class Meta:
        fields = ('regiaoIes', 'total')
