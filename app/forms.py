from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, DecimalField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired


class PropertyForm(FlaskForm):
    propertyTitle = StringField('Property Title', validators=[DataRequired()])
    propertyDesc = TextAreaField('Description', validators=[DataRequired()])
    no_of_bedrooms = IntegerField('No. of Bedrooms', validators=[DataRequired()])
    no_of_bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    propertyType = SelectField('Property Type', choices=[('House'),('Apartment')])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg','png'])])
