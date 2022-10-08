from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    """Класс форм для добавления задач.
    """
    title = StringField("Задача: ", validators=[DataRequired()])
    submit = SubmitField("+")
