from app import db


class Todo(db.Model):
    """Модель задач.(класс наследуется от моделей БД)

    Args:
        db : база данных инициализуруемая в __init__.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    priority = db.Column(db.Boolean)


# создается таблица в БД
db.create_all()
