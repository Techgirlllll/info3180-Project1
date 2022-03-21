from . import db

class Prop(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    propertyTitle = db.Column(db.String(255))
    propertyDesc = db.Column(db.String(500))
    no_of_bedrooms = db.Column(db.Integer)
    no_of_bathrooms = db.Column(db.Integer)
    price = db.Column(db.String(255))
    location = db.Column(db.String(255))
    propertyType = db.Column(db.String(255))
    photo = db.Column(db.String(255)) 
    

    def __init__ (self, propertyTitle,propertyDesc, no_of_bedrooms,no_of_bathrooms, price, location, propertyType, photo):
        self.propertyTitle =  propertyTitle
        self.propertyDesc = propertyDesc
        self.no_of_bedrooms = no_of_bedrooms
        self.no_of_bathrooms = no_of_bathrooms
        self.price = price
        self.location = location
        self.propertyType = propertyType
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
    
    def __repr__(self):
        return '<Property %r>' % (self.propertyTitle)
        
