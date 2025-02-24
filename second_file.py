from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ytrewq'


class LoginForm(FlaskForm):
    userid = StringField('ID астронавта', validators=[DataRequired()])
    password_1 = PasswordField('Пароль', validators=[DataRequired()])
    captainid = StringField('ID капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')
@app.route('/')
def index():
    return redirect("/login")

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())

@app.route('/list_prof/<type>')
def list_prof(type):
    jobs = ["пилот", "врач", "ученый", "штурман"]
    return render_template('jobs_list.html', type=type.lower(), professions=jobs)

@app.route('/auto_answer')
@app.route('/answer')
def auto_answer():
    profile = {}
    profile["title"] = "Ваша анкета миссии"
    profile["surname"] = "Борозинец"
    profile["name"] = "София"
    profile["education"] = "-"
    profile["profession"] = "-"
    profile["sex"] = "ж"
    profile["motivation"] = "-"
    profile["ready"] = "--"
    return render_template("auto_answer.html", **profile)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/distribution')
def distribution():
    return render_template('distribution.html', astro_list=["Ридли Скотт", "Марк Уотни", "Энди Уир"])


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')