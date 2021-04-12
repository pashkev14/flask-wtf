from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class FileForm(FlaskForm):
    field = FileField('Выбрать картинку', validators=[DataRequired()])
    submit = SubmitField('Отправить')
