from flask import Blueprint, redirect

default_api = Blueprint('default_api', __name__, url_prefix='/')

@default_api.route('/')
def default():
    return redirect("/api/1", code=302)
