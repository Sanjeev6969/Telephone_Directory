from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class SignUpForm(FlaskForm):
    name=StringField('Name')
    number=StringField('Number')
    submit=SubmitField('Submit')
    check=SubmitField('Check')
