import copy
import time
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

    @app.put("/api/put/workout/change_active_workout")
    def put_data(workout_id: WorkoutId = None):
        if workout_id is None:
            raise HTTPException(status_code=400, detail="MUST provide workout ID")

        id = workout_id.id
        data = load_data()
        workout = {}
        found = False

        for i in range(len(data['workouts'])):
            if data['workouts'][i]['id'] == id:
                found = True
                workout = data['workouts'][i]
                break

        if found is False:
            raise HTTPException(status_code=400, detail="Workout with corresponding ID was not found")

        data['active_workout']['name'] = workout['name']
        data['active_workout']['id'] = workout['id']
        data['active_workout']['start_date'] = time.time()
        data['active_workout']['exercises'] = []
        data['active_workout']['act_exercise'] = ""
        for exercise in workout['exercises']:
            data['active_workout']['exercises'].append({
                "name": exercise['name'],
                "nb_sets": exercise['nb_sets'],
                "nb_reps_low": exercise['nb_reps_low'],
                "nb_reps_high": exercise['nb_reps_high'],
                "list_weights": [],
                "list_reps": []
            })

        write_data(data)

    @app.put("/api/put/workout/update_active_workout")
    def put_app(workout_update: WorkoutUpdate = None):
        if workout_update is None:
            raise HTTPException(status_code=400, detail="MUST provide workout data")

        data = load_data()
        data['active_workout'] = workout_update.workout
        write_data(data)

    @app.put("/api/put/workout/end_active_workout")
    def put_app(workout_update: WorkoutUpdate = None):
        if workout_update is None:
            raise HTTPException(status_code=400, detail="MUST provide workout data")

        data = load_data()
        workout = workout_update.workout

        data['active_workout']['id'] = -1

        for wrkt in data['workouts']:
            if wrkt['id'] == workout['id']:
                for i in range(len(wrkt['exercises'])):
                    for j in range(len(workout['exercises'])):
                        if wrkt['exercises'][i]['name'] == workout['exercises'][j]['name']:
                            if len(workout['exercises'][j]['list_reps']) == 0:
                                continue
                            wrkt['exercises'][i]['list_reps'].insert(0, workout['exercises'][j]['list_reps'])
                            wrkt['exercises'][i]['list_weights'].insert(0, workout['exercises'][j]['list_weights'])
        write_data(data)
