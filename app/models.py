from . import db


class Properties(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String, nullable=False)
    property_type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo_filename = db.Column(db.String(100), nullable=False)

    def __init__(self, title, description, bedrooms, bathrooms, location, price, property_type, photo_filename):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.property_type = property_type
        self.photo_filename = photo_filename
