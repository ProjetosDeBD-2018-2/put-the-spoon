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
    'idTipoDespesa': fields.String,
    'tipo_despesa': fields.String,
    'nome_ies': fields.String,
    'sigla_ies': fields.String,
    'despesa_total': fields.Float
})

expenses_and_ratings = Model('ExpensesAndRatings', {
    'nome_ies': fields.String,
    'igcContinuo': fields.String,
    'DespesaTotal': fields.Float
})

values_by_region_rating = Model('ValuesByRegionRating', {
    'regiaoIes': fields.String,
    'nota': fields.Float
})

values_by_region = Model('ValuesByRegionExpenses', {
    'regiaoIes': fields.String,
    'despesa': fields.Float
})

expense_and_budget = Model('ExpenseAndBudget', {
    'idIes': fields.Integer,
    'nome_ies': fields.String,
    'orcamento': fields.Float,
    'despesa': fields.Float
})
