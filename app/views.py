from flask import redirect, render_template, url_for

from app import app, db
from app.forms import AddForm

from .models import Todo


@app.route('/', methods=['get', 'post'])
def home():
    """Функция представления домашней страницы.
    На домашней странице располагаются элементы формы AddForm,
    форма инициализируется в функции, далее в зависимости от типа запроса,
    либо формируются поля в шаблоне, либо проверяется введенная информация.
    При создании задачи по умолчанию некоторые поля модели получают
    дефолтные значения см. переменную new_todo.
    После создания функция возвращается с пустыми полями формы.
    Доступные адреса '/', доступные методы get/post. Указаны в декораторе.

    Returns:
        func: функции отображения домашней страницы.
    """
    todo_list = db.session.query(Todo).all()
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        new_todo = Todo(title=title, complete=False, priority=False)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('item.html', todo_list=todo_list, form=form)


@app.get('/update/<int:todo_id>')
def update(todo_id):
    """Функция обновления статуса выполнения.
    Адрес '/update/<int:todo_id>', указан в декораторе метода get.
    При получения запроса текущий статус меняется на противоположный.
    Поле модели типа boolen.

    Args:
        todo_id (int): идентификатор задачи.

    Returns:
        func: функция перенапрвления на главную страницу.
    """
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/priority/<int:todo_id>')
def priority(todo_id):
    """Функция определения приоритета задачи высокий/низкий.
    Адрес /priority/<int:todo_id>, указан в декораторе метода get.
    При получения запроса текущий приоритет меняется на противоположный.
    Поле модели типа boolen.

    Args:
        todo_id (int): идентификатор задачи.

    Returns:
        func: функция перенапрвления на главную страницу.
    """
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.priority = not todo.priority
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/delete/<int:todo_id>')
def delete(todo_id):
    """Функция удаления задачи.
    Адрес /delete/<int:todo_id>, указан в декораторе метода get.
    При получении запроса удаляет элемент БД с соответсвующим id.

    Args:
        todo_id (int): идентификатор задачи.

    Returns:
        func: функция перенапрвления на главную страницу.
    """
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))
