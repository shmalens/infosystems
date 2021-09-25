from flask import Flask, render_template, request, redirect
from pymysql import connect

# template_folder - параметр конструктора Flask,
# указывает директорию с шаблонами
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# passing argument in url
@app.route('/greeting/<name>')
def greeting_handler(name):
    return f'Hello {name}'


# passing arg with int val
@app.route('/users/<int:user_id>')
def search_user(user_id):
    users = [
        {'__id': 1, 'name': 'Sasha'},
        {'__id': 2, 'name': 'Ilia'},
        {'__id': 3, 'name': 'Artem'}
    ]
    for user in users:
        if user['__id'] == user_id:
            return user

    return 'User not found'


# Обработка GET параметров
# Вида url.domen/linking?name=name1&login=login1
# Чтобы обработать GET параметры, необходимо подключить ф-ю
# Flask request. A ф-я redirect перенаправит на определенную страницу
@app.route('/routing')
def routing():
    action = request.args.get('action', None)
    # Аналогичный код
    # if 'action' in request.args:
    #     action = request.args['action']
    # else:
    #     action = None

    actions = {'search': '/users/1', 'home': '/'}
    if action is not None:
        if action not in actions.keys():
            return f'Error, GET value {action} does not exist'
        return redirect(actions[action])

    return render_template('links.html')


# По умолчанию роут обрабатывает только GET
# Можно явно указать, какие методы HTML он обрабатывает
# @app.route("/form", methods=['GET', 'POST'])
# def form():
#     if request.method == 'GET':
#         return render_template('forms.html')
#     else:
#         login = request.form.get('login', None)
#         password = request.form.get('password', None)
#
#         if login and password:
#             if login == 'kek' and password == 'lol':
#                 return 'OK'
#             else:
#                 return 'Wrong login password'
#
#     return render_template('forms.html')

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('forms.html')
    else:
        login = request.form.get('login', None)
        password = request.form.get('password', None)

        connection = connect(host='127.0.0.1', user='root', password='CoWeNt11', port=3306)
        cursor = connection.cursor()
        _sql_request = f"select user_id, name from sem2.users where login='{login}' and password='{password}'"
        cursor.execute(_sql_request)
        res = cursor.fetchall()
        connection.close()

        if res:
            return str(res)

        else:
            return "Error ocured"


if __name__ == "__main__":
    app.run(host='localhost', port=5001)
