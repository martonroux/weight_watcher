from utils.write_data import write_data
from utils.load_data import load_data
from fastapi import HTTPException
from pydantic import BaseModel


class WorkoutUpdate(BaseModel):
    workout: dict


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
            data['workouts'].append(workout)
        write_data(data)
