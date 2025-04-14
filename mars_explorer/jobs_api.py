from flask import jsonify, Blueprint, make_response, request

from data import db_session
from data.jobs import Jobs

blueprint = Blueprint('jobs_api', __name__, template_folder='templates')

@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()

    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'teamleader', 'job', 'work_size', 'collaborators',
                                    'start_date', 'end_date', 'is_finished')) for item in jobs]
        }
    )

@blueprint.route('/api/jobs/<job_id>', methods=['GET'])
def get_one_job(job_id):
    try:
        job_id = int(job_id)
    except ValueError:
        return make_response(jsonify({'error': 'Invalid id'}), 400)
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'jobs': jobs.to_dict(only=('id', 'teamleader', 'job', 'work_size', 'collaborators',
                                               'start_date', 'end_date', 'is_finished'))})

@blueprint.route('/api/jobs/', methods=['POST'])
def create_job():
    print("BKK")
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in ['teamleader', 'job', 'collaborators', 'is_finished', 'work_size']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job=Jobs(
        job=request.json['job'],
        teamleader=request.json['teamleader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})


@blueprint.route('/api/jobs/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<job_id>', methods=['PUT'])
def edit_job(job_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    try:
        job_id = int(job_id)
    except ValueError:
        return make_response(jsonify({'error': 'Invalid id'}), 400)
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    jobs.job = request.json['job'] if 'job' in request.json else jobs.job
    jobs.teamleader = request.json['teamleader'] if 'teamleader' in request.json else jobs.teamleader
    jobs.work_size = request.json['work_size'] if 'work_size' in request.json else jobs.work_size
    jobs.collaborators = request.json['collaborators'] if 'collaborators' in request.json else jobs.collaborators
    jobs.is_finished = request.json['is_finished'] if 'is_finished' in request.json else jobs.is_finished
    db_sess.commit()
    return jsonify({'success': 'OK'})