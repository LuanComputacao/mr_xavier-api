from  app.models import db, Question, Item
from app import create_app
import uuid

app = create_app()
app.app_context().push()

# db.create_all(app=app)

question_code = '3kj45-3kj45hg-k3j4gg6g34jk-k3j4g5kg63kk'
question1 = Question(wording="Primeira questão do Banco de Questões. Gostou?",code=str(uuid.uuid4()))
question2 = Question(wording="Segunda questão do Banco de Questões. Gostou?",code=str(uuid.uuid4()))
item = Item(text='primeiro item de questão')
question1.items.append(item)

question_created = db.session.add(question1)
question_created = db.session.add(question2)

db.session.commit()
print(Question.query.all())