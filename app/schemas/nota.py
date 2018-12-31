from app.extensions import db


class Nota(db.Model):
    __tablename__ = 'Nota'
    idNota = db.Column(db.INT(), primary_key=True)
    anoNota = db.Column(db.INT())
    idIes = db.Column(db.INT())
    igcContinuo = db.Column(db.NVARCHAR(500))
    igcFaixa = db.Column(db.NVARCHAR(500))
