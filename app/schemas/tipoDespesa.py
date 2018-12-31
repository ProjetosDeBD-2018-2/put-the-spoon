from app.extensions import db


class TipoDespesa(db.Model):
    __tablename__ = 'TipoDespesa'
    id = db.Column(db.INT(), primary_key=True)
    tipo_despesa = db.Column(db.NVARCHAR(255))
