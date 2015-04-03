from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SigninForm(Form):
    idu = StringField('idu', validators=[DataRequired()])
    
