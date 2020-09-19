from  app.models import db, Question, Item
from app import create_app

app = create_app()
app.app_context().push()

db.create_all(app=app)

question = Question(wording="Primeira questão do Banco de Questões. Gostou?",code='3kj45-3kj45hg-k3j4gg6g34jk-k3j4g5kg63kk')
item = Item(text='primeiro item de questão')
question.items.append(item)

question_created = db.session.add(question)

db.session.commit()
print(question_created)
print(question)
print(item)