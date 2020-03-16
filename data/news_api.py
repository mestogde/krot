from flask import Blueprint, jsonify

from data import db_session
from data.jobs import Jobs

blueprint = Blueprint('news_api', __name__,
                      template_folder='templates')


@blueprint.route('/api/jobs')
def get_news():
    session = db_session.create_session()
    news = session.query(Jobs).all()
    return jsonify(
        {
            'erfrfe3erf':
                [item.to_dict(only=('id'))
                 for item in news]
        }
    )
