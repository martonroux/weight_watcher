from typing import List
from pydantic import BaseModel
import json


class Answer(BaseModel):
    description: str
    correct: bool


class Question(BaseModel):
    name: str
    answers: List[Answer]


class Quiz(BaseModel):
    questions: List[Question]


def put_janka_quiz(app):
    @app.put("/update-janka-quiz/")
    async def update_janka_quiz(quiz_data: Quiz):
        absolute_path_dist = "/home/ubuntu/janka-quiz/dist/quiz.json"
        absolute_path_pub = "/home/ubuntu/janka-quiz/public/quiz.json"

        try:
            with open(absolute_path_dist, "w") as f:
                json.dump(quiz_data.dict(), f)
        except Exception as e:
            return {"error": str(e)}

        try:
            with open(absolute_path_pub, "w") as f:
                json.dump(quiz_data.dict(), f)
            return {"message": "Quiz updated successfully"}
        except Exception as e:
            return {"error": str(e)}
