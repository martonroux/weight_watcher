from data_manager.workout_data import get_exercise_data, get_all_workouts, get_all_exercises, get_active_workout
from fastapi import HTTPException


def get_workout(app):
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
            "data": list_workouts['data']
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
            "data": list_exercises['data']
        }

    @app.get("/api/get/workout/get_exercise_data")              # GET DATA OF A SPECIFIC EXERCISE IN A SPECIFIC WORKOUT
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
            "error": "False",
            "data": workout_data['data']
        }

    @app.get("/api/get/workout/get_active_workout")
    def get_data():
        workout = get_active_workout()

        return {
            "error": "False",
            "data": workout
        }
