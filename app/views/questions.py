from flask import Blueprint
from app.models import Question

bp = Blueprint('questions', __name__, url_prefix='/questions')


@bp.route('/')
@bp.route('/<int:question_id>')
def list(question_id=None):
    return Question.get_delete_put_post(question_id)
