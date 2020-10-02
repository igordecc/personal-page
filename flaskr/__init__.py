import os

from flask import Flask

def create_app(test_config=None, *args, **kwargs):
    # app factory
    # create_app is global class object and very important

    app = Flask(__name__, instance_relative_config=True)  # futher is standart shaman setup to ubu-dubu defaults, lul
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, ' flaskr.postgresql')
    )

    if test_config is None:
        # load real config
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config
        app.config.from_mapping(test_config)
    # ensure instance folder exist. What is the instance anyway?
    try:
        os.makeddirs(app.instance_path)
    except OSError:
        print("no instance path, for some reason. Debug __init__.py")

    # simple page that says hello. We stopping on that, and making postgres now.
    @app.route('/hello')
    def hello():
        return 'Hello, World! And make me postgres output-> ___'

    # next part is initing db. It was sqlite. Now make postgres from it.
    """
    from . import db
    db.init_app(app)
    """
