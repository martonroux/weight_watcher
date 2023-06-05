from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from requests.get.get_body_weight import get_body_weight
from requests.get.get_workout import get_workout

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )


@app.get("/api/get")
def get_data():
    return "Hello world!"


get_body_weight(app)
get_workout(app)
