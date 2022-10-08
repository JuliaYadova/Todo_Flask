""" Приложение Todo.
    В данном файле инициализуется экземпляр приложения Flask,
    а также  инициализируются расширения.
    Указывается путь к настройкам среды и значение по умолчанию.
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV')
                       or 'config.DevelopementConfig')

# инициализирует расширения
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

# импортируются функции представления
from . import views
