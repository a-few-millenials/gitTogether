import os

from flask import Flask

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
	    # a default secret that should be overridden by instance config
	    SECRET_KEY='dev',
	    # store the database in the instance folder
	    DATABASE=os.path.join(app.instance_path, 'gitTogether.sqlite'),
    )

    if test_config is None:
	    # load the instance config, if it exists, when not testing
	    app.config.from_pyfile('config.py', silent=True)
    else:
	    # load the test config if passed in
	    app.config.update(test_config)
		
    # ensure the instance folder exists
    try:
	    os.makedirs(app.instance_path)
    except OSError:
	    pass
    
    # register the database commands
    from . import db
    db.init_app(app)
    
    from . import test
    app.register_blueprint(test.bp)
	
    """import gitTogether.views"""
    """
        Try and resolve issue with importing views from views.py
    """
    @app.route('/')
    def index():
        return 'Hello, World!'
		
    return app