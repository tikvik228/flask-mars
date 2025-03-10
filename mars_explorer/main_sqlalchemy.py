from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ytrewq'


def main():
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
def index():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    users = session.query(User).all()
    names = {str(u.id): (u.surname, u.name) for u in users}
    return render_template('index.html', jobs=jobs, names=names)

if __name__ == "__main__":
    main()