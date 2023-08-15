# Flask-SQLAlchemy

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import hashlib


from models import db, User
from forms import RegisterForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# инициализация БД
db.init_app(app)

app.config['SECRET_KEY'] = b'ea959bc6bbd140100d66503aa6ac1242c6eb0e8d4c38b85c7ea9a9d2a8e60451'
# получение csrf - объекта для работы с формами
csrf = CSRFProtect(app)



@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    # создать все таблицы
    db.create_all()
    # print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = to_hash(form.password.data)

        existing_user = User.query.filter((User.name == name) | (User.email == email)).first()

        if existing_user:
            error_msg = 'Username or email already exists.'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)

        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Registered success!'
    return render_template('register.html', form=form)

def to_hash(data):
    hash_obj = hashlib.new('sha256')
    hash_obj.update(data.encode())
    return hash_obj.hexdigest()



if __name__ == '__main__':
    # db.create_all()
    # with app.app_context(): 
    #     db.create_all()
    app.run(debug=True)
