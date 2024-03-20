from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    bedrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    bathrooms = IntegerField('No. of Bathrooms',
                             validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    property_type = SelectField('Property Type', choices=[(
        'House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo_filename = FileField('Photo', validators=[FileRequired(), FileAllowed(
        ['jpg', 'png', 'jpeg'], 'Images only!')])
