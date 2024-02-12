from wtforms import Form, StringField,TelField,IntegerField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email


class UserForm(Form):
    x1= IntegerField('x1')
    y1= IntegerField('y1')
    x2= IntegerField('x2')
    y2= IntegerField('y2')
    distancia= IntegerField('distancia')
class ResistenciaForm(Form):
    primerBanda= IntegerField('primerBanda')
    segundaBanda= IntegerField('segundaBanda')
    terceraBanda= IntegerField('terceraBanda')
    tolerancia= StringField('tolerancia')
    valor= IntegerField('valor')
    valorMax= IntegerField('valorMax')
    valorMin= IntegerField('valorMin')