from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


# Пример формы
# class ContactForm(FlaskForm):
#     name = StringField("Name: ", validators=[DataRequired()])
#     email = StringField("Email: ", validators=[Email()])
#     message = TextAreaField("Message", validators=[DataRequired()])
#     submit = SubmitField("Submit")


class AddForm(FlaskForm):
    title = StringField("Задача: ", validators=[DataRequired()])
    submit = SubmitField("+")
