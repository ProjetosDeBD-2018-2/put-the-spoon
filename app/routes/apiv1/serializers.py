from flask_restplus import fields, Model


ies_model = Model('Ies', {
    'cod_ies': fields.Integer,
    'nome_ies': fields.String,
    'sigla_ies': fields.String,
    'num_cnpj': fields.Integer,
    'tipo_organizacao': fields.String,
    'cod_mantenedora': fields.Integer,
    'email_ies': fields.String,
    'site_ies': fields.String
})

nota_model = Model('Nota', {
    'idNota': fields.Integer,
    'anoNota': fields.Integer,
    'idIes': fields.Integer,
    'igcContinuo': fields.String,
    'igcFaixa': fields.String,
})

expense_by_type = Model('ExpenseByType', {
    'idIes': fields.Integer,
    'idTipoDespesa': fields.String,
    'total': fields.Float
})

expenses_and_ratings = Model('ExpensesAndRatings', {
    'idIes': fields.Integer,
    'nome_ies': fields.String,
    'idNota': fields.Integer,
    'igcContinuo': fields.String,
    'idTipoDespesa': fields.String,
    'tipo_despesa': fields.String,
    'DespesaTotal': fields.Float
})

values_by_region = Model('ValuesByRegion', {
    'regiaoIes': fields.String,
    'total': fields.Float
})
