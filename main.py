from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal

app = FastAPI()

# Créer toutes les tables
models.Base.metadata.create_all(bind=engine)


# Modèles Pydantic
class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool


class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


# Connexion à la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Injection de dépendance
db_dependency = Annotated[SessionLocal, Depends(get_db)]


# Endpoints

# Ajouter une question avec ses choix
@app.post('/questions/')
def create_questions(question: QuestionBase, db: db_dependency):
    db_question = models.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    # Ajouter les choix
    for choice in question.choices:
        db_choice = models.Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id
        )
        db.add(db_choice)
    db.commit()

    # Retourner la question et ses choix créés
    return {"message": "Question and choices added successfully",
            "question": db_question.question_text,
            "choices": [{"choice_text": choice.choice_text, "is_correct": choice.is_correct} for choice in
                        question.choices]}


# Récupérer une question par ID
@app.get('/questions/{question_id}')
def read_questions(question_id: int, db: db_dependency):
    result = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    if not result:
        raise HTTPException(status_code=404, detail='Question is not found!')
    return result


# Récupérer les choix d'une question
@app.get('/choices/{question_id}')
def read_choices(question_id: int, db: db_dependency):
    result = db.query(models.Choices).filter(models.Choices.question_id == question_id).all()
    if not result:
        raise HTTPException(status_code=404, detail='Choices are not found!')
    return result
