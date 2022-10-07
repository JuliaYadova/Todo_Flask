from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV')
                       or 'config.DevelopementConfig')

# инициализирует расширения
db = SQLAlchemy(app)

from . import views
