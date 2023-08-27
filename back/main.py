from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_requests.get.get_body_weight import get_body_weight
from api_requests.get.get_workout import get_workout
from api_requests.put.put_workout import put_workout
from api_requests.put.put_body_weight import put_body_weight
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="../front/dist", html=True))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_data():
    return "Hello world!"


put_janka_quiz(app)     # TODO: REMOVE THIS?

get_body_weight(app)
get_workout(app)
put_workout(app)
put_body_weight(app)
