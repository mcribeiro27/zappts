from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import safe_str_cmp
from carta.models.cartas import Carta



param = reqparse.RequestParser()
param.add_argument('cartaId', type=int)
param.add_argument('remetente', type=str, help='O campo não pode ser nulo')
param.add_argument('password', type=str, help='O campo não pode ser nulo')
param.add_argument('conteudo')


class CartaResource(Resource):
    
    def get(self, cartaId):
        carta = Carta.find(cartaId)
        if carta:
            return carta.json(), 200
        return {'message': 'carta not found'}, 404

    @jwt_required()
    def put(self, cartaId):
        args = reqparse.RequestParser()
        args.add_argument('remetente')
        args.add_argument('password')
        args.add_argument('conteudo')

        dados = args.parse_args()
        carta_find = Carta.find(cartaId)

        if carta_find:
            carta_find.update(**dados)
            try:
                carta_find.save()
            except:
                return {'message': 'Houve um erro interno no servidor ao Salvar a carta'}, 500
            return carta_find.json(), 200 # Success

        carta = Carta(cartaId, **dados)
        try:
            carta.save()
        except:
            return {'message': 'Houve um erro interno no servidor ao Salvar a carta'}, 500 # INTERNAL ERROR
        return carta.json(), 201 # Created

    @jwt_required()
    def delete(self, cartaId):
        carta = Carta.find(cartaId)
        if carta:
            carta.delete()
            return {'message': 'carta deleted.'}, 200
        return {'message': 'carta not found'}, 404


class CartasResource(Resource):
    def get(self):
        return {'cartas': [carta.json() for carta in Carta.query.all()]}

    
    def post(self):
        dados = param.parse_args()
        carta = Carta(**dados)
        if Carta.find(dados['cartaId']):
            return {'message': f'id {dados["cartaId"]} already exists'}, 400
        try:
            carta.save()
        except:
            return {'message': 'there was an internal server error while saving the carta.'}, 500
        return carta.json(), 201


class Authenticate(Resource):
    """ 
        Classe para login no sitema

    """
    @classmethod
    def post(cls):

        arg = reqparse.RequestParser()
        arg.add_argument('remetente')
        arg.add_argument('password')

        dados = arg.parse_args()
        carta = Carta.find_by_remetente(dados['remetente'])

        if carta and safe_str_cmp(carta.password, dados['password']):
            token = create_access_token(identity=carta.cartaId)
            return {'access_token': token}, 200
        return {'message': 'remetente or password is incorrect!'}, 401
