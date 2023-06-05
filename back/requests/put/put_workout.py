from main import app


@app.put("/api/put/workout/create_workout")
def put_data(workout_name: str):
    return {}
