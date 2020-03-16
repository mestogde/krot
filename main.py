from flask import render_template, Flask, redirect
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from flask_restful import Api
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

from data import db_session
from data.users import User
from data import news_api
from data import news_rescources

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_exploers.db")
app = Flask(__name__)
api = Api(app)
url = "http://127..0.0.1:8080/"


# для списка объектов
api.add_resource(news_rescources.UsersListResource, '/api/v2/news')

# для одного объекта
api.add_resource(news_rescources.UsersResource, '/api/v2/news/<int:news_id>')


if __name__ == '__main__':
    app.run()