from . import db 

#Usuário
class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    wpp = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    
    order = db.relationship('Pedido', backref='usuatio', lazy= True)
    
