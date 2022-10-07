from flask import redirect, render_template, request, url_for, abort

from app import app, db
from app.forms import AddForm

from .models import Todo

@app.route('/', methods=['get', 'post'])
# @app.get('/')
def home():
    todo_list = db.session.query(Todo).all()
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        new_todo = Todo(title=title, complete=False, priority=False)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('item.html', todo_list=todo_list, form=form)


# @app.post('/add')
# def add():
#     form = AddForm()
#     if form.validate_on_submit():
#         title = form.title.data
#         new_todo = Todo(title=title, complete=False, priority=False)
#         db.session.add(new_todo)
#         db.session.commit()
#         return redirect(url_for('home'))
#     else:
#         abort(406)


@app.get('/update/<int:todo_id>')
def update(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/priority/<int:todo_id>')
def priority(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.priority = not todo.priority
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/delete/<int:todo_id>')
def delete(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))
