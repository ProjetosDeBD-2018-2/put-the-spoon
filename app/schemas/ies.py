from app.extensions import db
from app.extensions import ma


class Ies(db.Model):
    __tablename__ = 'Ies'
    cod_ies = db.Column(db.INT(), primary_key=True)
    nome_ies = db.Column(db.Text())
    sigla_ies = db.Column(db.Text())
    num_cnpj = db.Column(db.BigInteger())
    tipo_organizacao = db.Column(db.Text())
    cod_mantenedora = db.Column(db.Integer())
    email_ies = db.Column(db.Text())
    site_ies = db.Column(db.Text())


class ExpenseByTypeSchema(ma.Schema):
    class Meta:
        fields = (
            'idIes',
            'nome_ies',
            'idTipoDespesa',
            'tipo_despesa',
            'despesa'
        )


class ExpensesAndRatingsSchema(ma.Schema):
    class Meta:
        fields = (
            'nome_ies',
            'igcContinuo',
            'DespesaTotal'
        )
