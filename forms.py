from wtforms import Form, StringField,TelField,IntegerField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email


class UserForm(Form):
    x1= IntegerField('x1')
    y1= IntegerField('y1')
    x2= IntegerField('x2')
    y2= IntegerField('y2')
    distancia= IntegerField('distancia')
