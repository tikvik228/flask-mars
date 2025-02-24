from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

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


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')