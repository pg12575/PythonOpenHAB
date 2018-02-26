from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class IDForm(FlaskForm):
    ID = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Submit')