from app.extensions import db


class Endereco(db.Model):
    __tablename__ = 'Endereco'
    id = db.Column(db.INT(), primary_key=True)
    logradouro = db.Column(db.TEXT())
    numero = db.Column(db.TEXT())
    complemento = db.Column(db.TEXT())
    bairro = db.Column(db.TEXT())
    municipio = db.Column(db.TEXT())
    nomeUF = db.Column(db.TEXT())
    siglaUF = db.Column(db.TEXT())
    cep = db.Column(db.INT())
    regiaoIes = db.Column(db.TEXT())
    localizacaoIes = db.Column(db.TEXT())
    cod_ies = db.Column(db.INT())
    sigla_ies = db.Column(db.TEXT())
