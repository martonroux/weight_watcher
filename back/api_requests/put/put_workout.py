from utils.write_data import write_data
from utils.load_data import load_data
from fastapi import HTTPException
from pydantic import BaseModel


class WorkoutUpdate(BaseModel):
    workout: dict


class WorkoutId(BaseModel):
    id: int


def put_workout(app):
    @app.put("/api/put/workout/update_workout")
    def put_data(workout_update: WorkoutUpdate = None):
        if workout_update is None:
            raise HTTPException(status_code=400, detail="MUST provide workout data")
        workout = workout_update.workout
        data = load_data()
        wrkt_id = workout['id']
        found = False

        for i in range(len(data['workouts'])):
            if data['workouts'][i]['id'] == wrkt_id:
                data['workouts'][i] = workout
                found = True
                break

        if found is False:
            raise HTTPException(status_code=400, detail="Workout doesn't exist yet, or ID was changed (forbidden)")
        write_data(data)

    @app.put("/api/put/workout/add_workout")
    def put_data(new_workout: WorkoutUpdate = None):
        if new_workout is None:
            raise HTTPException(status_code=400, detail="MUST provide workout data")

        workout = new_workout.workout
        wrkt_id = workout['id']
        data = load_data()
        found = False

        for i in range(len(data['workouts'])):
            if data['workouts'][i]['id'] == wrkt_id:
                found = True
                break

        if found is True:
            raise HTTPException(status_code=400, detail="Workout already exist with same ID.")

        data['workouts'].append(workout)
        write_data(data)

    @app.put("/api/put/workout/delete_workout")
    def put_data(workout_id: WorkoutId = None):
        if workout_id is None:
            raise HTTPException(status_code=400, detail="MUST provide workout ID")

        id = workout_id.id
        data = load_data()
        found = False

        for i in range(len(data['workouts'])):
            if data['workouts'][i]['id'] == id:
                data['workouts'].remove(data['workouts'][i])
                found = True
                break

        if found is False:
            raise HTTPException(status_code=400, detail="Workout with corresponding ID was not found")

        write_data(data)
