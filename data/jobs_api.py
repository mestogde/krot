from flask import Blueprint, jsonify
from data import db_session
from data.jobs import Jobs


blueprint = Blueprint('jobs_api', __name__,
                            template_folder='templates')



@blueprint.route('/api/jobs')
def get_news():
    session = db_session.create_session()
    news = session.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators',
                                    'start_date', 'end_date', 'is_finished', 'user_id', 'user'))
                 for item in news]
        }
    )