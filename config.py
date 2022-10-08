"""Настройки приложения.
"""
import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Создается базовый класс настроект приложения.
    Устанавливается SECRET_KEY (или по умолчанию) и
    отключены уведолмления о изменениях в БД.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopementConfig(BaseConfig):
    """Дочерний класс настроек для стадии разработки.
    Устанавливается режим отладки и данные БД для разработки.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or \
        'sqlite:///db.sqlite'


class TestingConfig(BaseConfig):
    """Дочерний класс настроек для стадии тестирования.
    Устанавливается режим отладки и данные БД для тестов.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or \
        'sqlite:///db.sqlite'


class ProductionConfig(BaseConfig):
    """Дочерний класс настроек для стадии тестирования.
    Отключается режим отладки и передаются данные БД для продакта.
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or \
        'sqlite:///db.sqlite'
