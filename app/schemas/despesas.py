from app.extensions import db
from app.extensions import ma


class Despesas(db.Model):
    __tablename__ = 'Despesas'
    id = db.Column(db.INT(), primary_key=True)
    ano_mes_lancamento = db.Column(db.NVARCHAR(500))
    codigo_orgao_superior = db.Column(db.NVARCHAR(500))
    nome_orgao_superior = db.Column(db.NVARCHAR(500))
    codigo_orgao_subordinado = db.Column(db.NVARCHAR(500))
    nome_orgao_subordinado = db.Column(db.NVARCHAR(500))
    codigo_unidade_gestora = db.Column(db.NVARCHAR(500))
    nome_unidade_gestora = db.Column(db.NVARCHAR(500))
    codigo_gestao = db.Column(db.NVARCHAR(500))
    nome_gestao = db.Column(db.NVARCHAR(500))
    codigo_unidade_orcamentaria = db.Column(db.NVARCHAR(500))
    nome_unidade_orcamentaria = db.Column(db.NVARCHAR(500))
    codigo_funcao = db.Column(db.NVARCHAR(500))
    nome_funcao = db.Column(db.NVARCHAR(500))
    codigo_subfuncao = db.Column(db.NVARCHAR(500))
    nome_subfuncao = db.Column(db.NVARCHAR(500))
    codigo_programa_orcamentario = db.Column(db.NVARCHAR(500))
    nome_programa_orcamentario = db.Column(db.NVARCHAR(500))
    codigo_acao = db.Column(db.NVARCHAR(500))
    nome_acao = db.Column(db.NVARCHAR(500))
    idTipoDespesa = db.Column(db.NVARCHAR(500))
    idRubrica = db.Column(db.INT())
    idIes = db.Column(db.INT())


class RegionsWithExpenses(ma.Schema):
    class Meta:
        fields = ('regiaoIes', 'despesa')
