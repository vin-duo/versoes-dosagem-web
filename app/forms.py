from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired

class Dosagem(FlaskForm):
    piloto = FloatField('Traço Piloto (m)', validators = [DataRequired()])
    rico = FloatField('Traço Rico (m):', validators =[DataRequired()])
    pobre = FloatField('Traço Pobre (m)', validators =[DataRequired()])
    pesobrita = FloatField('Peso da brita', validators=[DataRequired()])
    cp = FloatField('CP', validators=[DataRequired()])
    slump = FloatField('Abatimento desejado (Slump)', validators=[DataRequired()])
    submit = SubmitField('Registrar')


class Piloto(FlaskForm):
    argamassa = FloatField('Alfa')
    submit = SubmitField('Criar')







