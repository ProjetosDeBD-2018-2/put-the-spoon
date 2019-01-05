from app.extensions import db
from app.extensions import ma


class Orcamento(db.Model):
    __tablename__ = 'Orcamento'
    id = db.Column(db.INT(), primary_key=True)
    exercicio = db.Column(db.NVARCHAR(500))
    codigo_orgao_superior = db.Column(db.NVARCHAR(500))
    nome_orgao_superior = db.Column(db.NVARCHAR(500))
    codigo_orgao_subordinado = db.Column(db.NVARCHAR(500))
    nome_orgao_subordinado = db.Column(db.NVARCHAR(500))
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
    codigo_categoria_economica = db.Column(db.NVARCHAR(500))
    nome_categoria_economica = db.Column(db.NVARCHAR(500))
    codigo_grupo_de_despesa = db.Column(db.NVARCHAR(500))
    nome_grupo_de_despesa = db.Column(db.NVARCHAR(500))
    codigo_elemento_de_despesa = db.Column(db.NVARCHAR(500))
    nome_elemento_de_despesa = db.Column(db.NVARCHAR(500))
    orcamento_inicial = db.Column(db.FLOAT())
    orcamento_atualizado = db.Column(db.FLOAT())
    orcamento_realizado = db.Column(db.FLOAT())
    idIes = db.Column(db.INT())


class HighestExpenseByTypeDespesa(ma.Schema):
    class Meta:
        fields = ('idIes', 'nome_ies', 'orcamento', 'total')
