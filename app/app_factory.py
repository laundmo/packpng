from flask import Flask

from .extensions import limiter, cache

from .main import main_blueprint
from .redeploy import redeploy_blueprint

def create_app():
    app = Flask(__name__)
    
    limiter.init_app(app)
    cache.init_app(app)
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(redeploy_blueprint)
    
    return app
