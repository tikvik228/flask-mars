from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ytrewq'


def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()

    info = {"surname": ["Scott", "Watney", "Lewis", "Vogel"],
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
        session.add(user)

    session.commit()

if __name__ == "__main__":
    main()