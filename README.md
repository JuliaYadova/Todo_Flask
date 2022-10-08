
# Todo_Flask
<div id="header" align="left">
  <img src=https://media.giphy.com/media/Wrlwh4k4Uz1o3imeZg/giphy.gif width="100"/>
</div>

---
### Стек:

<div align="left">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python 3" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/flask/flask-original-wordmark.svg" title="Flask" alt="Flask" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original-wordmark.svg" title="SQLite3" alt="SQLite3" width="40"   height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg"  title="CSS3" alt="CSS" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
</div>


## Описание проекта
   Сайт для создания списка дел. Возможна приоритезация задач выская/низкая.



## Подготовка и запуск проекта

1. Копирование репозитория
Скопируйте репозиторий на локальную машину.

2. Установка на локальную машину:

 + Зайдите в папку приложения (где расположен файл runner) и выполните команды:
   
   *По умолчания система машины Windows, для других систем команды уcтановки вируального окружения и другие могут незначительно отличаться.
   ```
    python -m venv venv
    source venv/Scripts/activate
    python -m pip install -r requirements.txt
    python runner.py runserver

   ```
 + Откройте указанный адрес в браузере:
   
   *Вывод в консоли с адресом выглядит так:
   ```
   * Serving Flask app 'app'
   * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on http://127.0.0.1:5000  # Вот адрес
   Press CTRL+C to quit
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 
   ```
 + Проект запущен.
   
## Инструкция по использованию
 + Для записи задачи необходимо в поле под текстом Tasks внести соотвествующую запись, далее нажать на плюс.
   По умолчанию приоритет ставится низкий для измения нажать на кнопку 'важно' или 'не важно', если нужно понизить приоритет.

 + Для пометки задачи как выполненной нажать на кнопку выполнено, задача станет зачеркнутой и появится кнопка для удаления,
   если необходимо вернуть задаче статус 'не выполненно' нажать на соответсующую кнопку.
 
 + Задачи отражаются на странице по приоритету и далее по статусу выполнения.
---
## Автор:
Ядова Юлия
