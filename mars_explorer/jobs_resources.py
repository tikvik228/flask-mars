from data import db_session
from flask import jsonify
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash
from data.jobs import Jobs
from data.reqparse_job import parser


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"работа с id {job_id} не найдена")

def abort_if_job_id_not_int(job_id):
    try:
        job_id = int(job_id)
    except ValueError:
        abort(404, message=f"id работы должен быть числом")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_id_not_int(job_id)
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(only=('teamleader', 'job', 'work_size', 'collaborators', 'is_finished'))})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs_list = session.query(Jobs).all()
        return jsonify({'jobs': [i.to_dict(only=('teamleader', 'job', 'work_size', 'collaborators', 'is_finished'))
                                 for i in jobs_list]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            teamleader=args['teamleader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'id': job.id})