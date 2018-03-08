from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class IDForm(FlaskForm):
    ID = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Tasker(FlaskForm):
    submit1 = SubmitField('Task A')
    submit2 = SubmitField('Task B')

class exitApp(FlaskForm):
    submit3 = SubmitField('Exit')