from carta.ext.database import db


class Carta(db.Model):
    __tablename__ = 'carta'

    cartaId = db.Column(db.Integer, primary_key=True)
    remetente = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.Text)

    def __init__(self, cartaId, remetente, password, conteudo):
        self.cartaId = cartaId
        self.remetente = remetente
        self.password = password
        self.conteudo = conteudo

    def json(self):

        return {
            'cartaId': self.cartaId,
            'remetente': self.remetente,
            'password': self.password,
            'conteudo': self.conteudo
        }

    @classmethod
    def find(cls, cartaId):
        carta = cls.query.filter_by(cartaId=cartaId).first()
        if carta:
            return carta
        return None

    @classmethod
    def find_by_remetente(cls, remetente):
        carta = cls.query.filter_by(remetente=remetente).first()
        if carta:
            return carta
        return None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, remetente, password, conteudo):
        self.remetente = remetente
        self.password = password
        self.conteudo = conteudo

    def delete(self):
        db.session.delete(self)
        db.session.commit()