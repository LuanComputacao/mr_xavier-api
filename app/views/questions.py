from flask import Blueprint, request
from app.models import Question

bp = Blueprint('questions', __name__, url_prefix='/questions')


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/<int:question_id>', methods=['GET', 'PUT'])
def list(question_id=None):
    print(request.data)
    return Question.get_delete_put_post(question_id)
