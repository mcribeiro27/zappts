from flask import Blueprint
from flask_restful import Api

from .carta import CartaResource, CartasResource, Authenticate


bp = Blueprint('api', __name__, url_prefix='/carta')
api = Api(bp)

def init_app(app):
    api.add_resource(CartaResource, '/<int:cartaId>')
    api.add_resource(CartasResource, '')
    api.add_resource(Authenticate, '/login')
    
    app.register_blueprint(bp)