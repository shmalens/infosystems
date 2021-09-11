from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)


@app.route('/')  # => http://127.0.0.1:5001
def index():
    return 'hello from flask'


@app.route('/greeting')
def greeting_handler():
    return 'hello im flask'


@app.route('/info')
def info_handler():
    return f'Now: {datetime.now()}, PID: {os.getpid()}'


@app.route('/home')
def home_page_handler():
    return render_template('index.html')

# Передача параметров в явном виде
# @app.route('/home-dynamic')
# def home_page_dynamic_handler():
#     return render_template('dynamic.html', name='dfdfdfd', list_items=[5, 6, -3, 5, 'dfdf'])


# Передача параметров через контекст в виде словаря
@app.route('/home-dynamic')
def home_page_dynamic_handler():
    context = {
        'name': 'Ivan',
        'list_items': ['a', 'b', 'c'],
        'today': datetime.now()
    }
    return render_template('dynamic.html', **context)


@app.route('/child')
def child_page_handler():
    return render_template('child.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
