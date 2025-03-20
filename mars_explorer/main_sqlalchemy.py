from flask_login import LoginManager, login_user, logout_user, login_required
from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.register import RegisterForm
from data.login_form import LoginForm
from data.add_job import AddJobForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ytrewq'
login_manager = LoginManager()
login_manager.init_app(app)


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
    names = {str(u.id): (u.surname, u.name) for u in users}
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
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/addjob',  methods=['GET', 'POST'])
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
if __name__ == "__main__":
    main()