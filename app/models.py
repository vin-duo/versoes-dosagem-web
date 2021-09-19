from app import db

class Parametros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alfa = db.Column(db.Integer, index=True, unique=True)

    c_unitario = db.Column(db.Integer)
    a_unitario = db.Column(db.Integer)
    b_unitario = db.Column(db.Integer)
    
    c_massa = db.Column(db.Integer)
    a_massa = db.Column(db.Integer)
    b_massa = db.Column(db.Integer)
    
    c_acr = db.Column(db.Integer)
    a_acr= db.Column(db.Integer)
    
    agua = db.Column(db.Integer)

    
    def __repr__(self):
        return'<valores {}, {}, {}, {}, {}, {}, {}, {}, {}, {}>\n'.format(self.alfa, self.c_unitario, self.a_unitario, self.b_unitario, self.c_massa, self.a_massa, self.b_massa, self.c_acr, self.a_acr, self.agua)


class Padrao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    piloto = db.Column(db.Integer, unique=True)
    rico = db.Column(db.Integer, unique=True)
    pobre = db.Column(db.Integer, unique=True)
    cp = db.Column(db.Integer)
    pesobrita = db.Column(db.Integer)
    slump = db.Column(db.Integer)
    
    def __repr__(self):
        return'\n<valores {} {} {} {} {} {} >'.format(self.piloto, self.rico, self.pobre, self.cp, self.pesobrita, self.slump)























'''
class Add_alfa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teor_argamassa = db.Column(db.Numeric(1,2), nullable=False)
    a = db.Column(db.Integer, nullable=False)
    b = db.Column(db.Numeric(5,2), nullable=False)
    a_massa = db.Column(db.Numeric(5,2), nullable=False)
    b_massa = db.Column(db.Numeric(5,2), nullable=False)
'''
    
#    def __repr__(self):
#        return'<Parametro aLFa {}'.format(self.alfa) 

    