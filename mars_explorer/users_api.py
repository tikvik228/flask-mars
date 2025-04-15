from flask import jsonify, Blueprint, make_response, request

from data import db_session
from data.users import User

blueprint = Blueprint('users_api', __name__, template_folder='templates')


@blueprint.route('/api/users', methods=['GET'])
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()

    return jsonify(
        {
            'users':
                [item.to_dict(only=('id', 'surname', 'name', 'age', 'position',
                                    'speciality', 'address', 'email', 'hashed_password', 'modified_date')) for item in users]
        }
    )


@blueprint.route('/api/users/<user_id>', methods=['GET'])
def get_one_user(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        return make_response(jsonify({'error': 'Invalid id'}), 400)
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(user_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'users': users.to_dict(only=('id', 'surname', 'name', 'age', 'position',
                    'speciality', 'address', 'email', 'hashed_password', 'modified_date'))})


@blueprint.route('/api/users/', methods=['POST'])
def create_user():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    if db_sess.query(User).filter(User.email == request.json['email']).first():
        return make_response(jsonify({'error': 'Email already exist'}), 409)
    user=User(
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        address=request.json['address'],
        email=request.json['email'],
        speciality=request.json['speciality'],
    )
    user.set_password(request.json['hashed_password'])
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'id': user.id})


@blueprint.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<user_id>', methods=['PUT'])
def edit_user(user_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    try:
        user_id = int(user_id)
    except ValueError:
        return make_response(jsonify({'error': 'Invalid id'}), 400)
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(user_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    users.surname = request.json['surname'] if 'surname' in request.json else users.surname
    users.name = request.json['name'] if 'name' in request.json else users.name
    users.age = request.json['age'] if 'age' in request.json else users.age
    users.position = request.json['position'] if 'position' in request.json else users.position
    users.speciality = request.json['speciality'] if 'speciality' in request.json else users.speciality
    users.address = request.json['address'] if 'address' in request.json else users.address
    users.email = request.json['email'] if 'email' in request.json else users.email
    if 'hashed_password' in request.json:
        users.set_password(request.json['hashed_password'])
    db_sess.commit()
    return jsonify({'success': 'OK'})