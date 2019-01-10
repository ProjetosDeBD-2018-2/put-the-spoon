from app.extensions import db


class Rubrica(db.Model):
    __tablename__ = 'Rubrica'
    id = db.Column(db.INT(), primary_key=True)
    codigo_rubrica = db.Column(db.NVARCHAR(500))
    descricao_rubrica = db.Column(db.NVARCHAR(500))
    valor_empenhado_reais = db.Column(db.FLOAT())
    valor_liquido_reais = db.Column(db.FLOAT())
    valor_pago_reais = db.Column(db.FLOAT())
    id_despesa = db.Column(db.INT())
