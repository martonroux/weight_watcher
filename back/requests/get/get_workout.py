from data_manager.workout_data import get_exercise_data, get_all_workouts, get_all_exercises
from main import app
from fastapi import HTTPException


@app.get("/api/get/workout/get_all_workouts")                       # GET LIST OF EXISTING WORKOUTS
def get_data():
    list_workouts = get_all_workouts()
    if list_workouts['error'] is not "False":
        raise HTTPException(                                        # ERROR IF GET_ALL_WORKOUTS RETURNS ERROR
            status_code=400,
            detail=list_workouts['error']
        )
    return {
        "error": "False",
        "data": {
            "list": []
        }
    }


@app.get("/api/get/workout/get_all_exercises")                      # GET LIST OF EXISTING EXERCISES IN WORKOUT
def get_data(workout: str = None):
    if workout is None:
        raise HTTPException(                                        # ERROR IF WORKOUT IS NONE
            status_code=400,
            detail="Workout variable MUST be provided."
        )
    list_exercises = get_all_exercises(workout)
    if list_exercises['error'] is not "False":
        raise HTTPException(                                        # ERROR IF GET_ALL_EXERCISES RETURNS ERROR
            status_code=400,
            detail=list_exercises['error']
        )
    return {
        "error": "False",
        "data": {
            "workout": workout,
            "list": list_exercises['list']
        }
    }


@app.get("/api/get/workout/get_exercise_data")                  # GET DATA OF A SPECIFIC EXERCISE IN A SPECIFIC WORKOUT
def get_data(workout: str = None, exercise: str = None):
    if workout is None:
        raise HTTPException(                                        # ERROR IF WORKOUT IS NONE
            status_code=400,
            detail="Workout variable MUST be provided."
        )
    if exercise is None:
        raise HTTPException(                                        # ERROR IF EXERCISE IS NONE
            status_code=400,
            detail="Exercise variable MUST be provided."
        )

    workout_data = get_exercise_data(workout, exercise)
    if workout_data["error"] is not "False":
        raise HTTPException(                                        # ERROR IF GET_EXERCISE_DATA RETURNS ERROR
            status_code=400,
            detail=workout_data["error"]
        )

    return {
        "errors": "False",
        "data": {
            workout_data['list']
        }
    }
