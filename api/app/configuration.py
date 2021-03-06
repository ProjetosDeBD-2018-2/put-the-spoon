import os
import ast

import app as app_root


class BaseConfig(object):
    '''
    FILES CONFIG
    '''
    APP_FOLDER = os.path.abspath(os.path.dirname(app_root.__file__))
    STATIC_FOLDER = os.path.join(APP_FOLDER, 'static')

    '''
    DATABASE CONFIG
    '''
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://root@localhost/putthespoon_dev')

    '''
    FLASK RESTPLUS CONFIG
    '''
    RESTPLUS_MASK_SWAGGER = ast.literal_eval(os.getenv('MASK_SWAGGER', 'False'))
