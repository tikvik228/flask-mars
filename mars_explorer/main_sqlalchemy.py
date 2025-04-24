from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask import Flask, render_template, redirect, request, abort, Blueprint, make_response, jsonify
from flask_restful import Api
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.register import RegisterForm
from data.login_form import LoginForm
from data.add_job import AddJobForm
import jobs_api
import users_api
from users_resources import UserListResource, UsersResource
from jobs_resources import JobsResource, JobsListResource
from requests import get
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ytrewq'
login_manager = LoginManager()
login_manager.init_app(app)
api = Api(app)
'''db_session.global_init("db/mars_explorer.db")
blueprint = Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates')'''

def main():
    db_session.global_init("db/mars_explorer.db")
    '''db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    new_job = Jobs()
    new_job.teamleader = 1
    new_job.job = "deployment of residential modules 1 and 2"
    new_job.work_size = 15
    new_job.collaborators = "2, 3"
    new_job.is_finished = False
    session.add(new_job)
    session.commit()'''
    '''info = {"surname": ["Scott", "Watney", "Lewis", "Vogel"],
            "name": ["Ridley", "Mark", "Melissa", "Alex"],
            "age": [21, 31, 34, 42],
            "position": ["captain", "crew", "commander", "navigator"],
            "speciality": ["research engineer", "botanist", "Submarine Warfare officer, oceanographer", "chemist"],
            "address": ["module_1", "module_4", "module_1", "module_2"],
            "email": ["scott_chief@mars.org", "potato220@mars.org", "aresIII@mars.org", "hardcore_mode@mars.org"],
            "hashed_password": ["cap", "potato", "disco_style", "Magnesium-based_Lifeform"]}

    for i in range(len(info["surname"])):
        user = User()
        user.surname = info["surname"][i]
        user.name = info["name"][i]
        user.age = info["age"][i]
        user.position = info["position"][i]
        user.speciality = info["speciality"][i]
        user.address = info["address"][i]
        user.email = info["email"][i]
        user.hashed_password = info["hashed_password"][i]
        user.set_password(user.hashed_password)
        session.add(user)'''
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    # для списка объектов
    api.add_resource(UserListResource, '/api/v2/users')
    # для одного объекта
    api.add_resource(UsersResource, '/api/v2/users/<user_id>')
    # для списка объектов
    api.add_resource(JobsListResource, '/api/v2/jobs')
    # для одного объекта
    api.add_resource(JobsResource, '/api/v2/jobs/<job_id>')
    app.run()
@app.route('/')
def base():
    return render_template('base.html')

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/index')
def index():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    users = session.query(User).all()
    names = {u.id: (u.surname, u.name) for u in users}
    return render_template('index.html', jobs=jobs, names=names)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("dd")
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Register', form=form,
                                   message="Введенные пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Register', form=form,
                                   message="Пользователь с таким логином уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            email=form.email.data,
            speciality=form.speciality.data,
            address=form.address.data,
            city_from=form.city_from.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/add_job',  methods=['GET', 'POST'])
def addjob():
    add_form = AddJobForm()
    if add_form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs(
            job=add_form.job.data,
            teamleader=add_form.team_leader.data,
            work_size=add_form.work_size.data,
            collaborators=add_form.collaborators.data,
            is_finished=add_form.is_finished.data
        )
        db_sess.add(jobs)
        db_sess.commit()
        return redirect('/index')
    return render_template('add_job.html', title='Adding job',form=add_form)

@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def job_edit(id):
    form = AddJobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.teamleader == current_user.id) | (
                                                      current_user.id == 1)).first()
        if jobs:
            form.job.data = jobs.job
            form.team_leader.data = jobs.teamleader
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          (Jobs.teamleader == current_user.id) | (
                                                      current_user.id == 1)).first()
        if jobs:
            jobs.job = form.job.data
            jobs.teamleader = form.team_leader.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_job.html', title='Job Edit', form=form)

@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def job_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      (Jobs.teamleader == current_user.id) | (
                                              current_user.id == 1)).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')

@app.route('/users_show/<int:user_id>', methods=['GET'])
def users_show(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        abort(400)
    name_of_city = get(f'http://localhost:5000/api/users/{user_id}').json()["users"]["city_from"]
    name_and_surname = get(f'http://localhost:5000/api/users/{user_id}').json()["users"]["name"] + " " + \
        get(f'http://localhost:5000/api/users/{user_id}').json()["users"]["surname"]
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": name_of_city,
        "format": "json"}

    response = get(geocoder_api_server, params=geocoder_params)

    if not response:
        print("oops")
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    delta = "0.005"
    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta, delta]),
        "z": 10,
        "apikey": apikey,
        "maptype": 'admin',
        "theme": "dark"
    }
    '''map_params = {"ll": ','.join(map(str, self.map_ll)),
                  "z": self.map_zoom,
                  "theme": self.theme,
                  "maptype": self.map_l,
                  "lang": "ru_RU",
                  "pt": ','.join(map(str, self.point_marker)),
                  "apikey": self.api_key}'''

    map_api_server = "https://static-maps.yandex.ru/v1"
    # ... и выполняем запрос
    response = get(map_api_server, params=map_params)
    way_to_img = 'flask_evgen/mars_explorer/static/image/home_img.png'
    with open('static/image/home_img.png', mode="wb") as file:
        file.write(response.content)
    return render_template('users_home.html', name=name_and_surname)
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

if __name__ == '__main__':
    main()
