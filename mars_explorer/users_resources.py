from data import db_session
from flask import jsonify
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash
from data.users import User
from data.reqparse_user import parser


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f"пользователь с id {user_id} не найден")

def abort_if_user_id_not_int(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        abort(404, message=f"id пользователя должен быть числом")

def set_password(password):
    return generate_password_hash(password)


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_id_not_int(user_id)
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'user': users.to_dict(only=('name', 'surname', 'age', 'position', 'speciality',
                                                    'address', 'email', 'hashed_password'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'user': [i.to_dict(only=('name', 'surname', 'age', 'position', 'speciality',
                                                    'address', 'email', 'hashed_password')) for i in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            email=args['email'],
            address=args['address'],
            hashed_password=args['hashed_password']
        )
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})