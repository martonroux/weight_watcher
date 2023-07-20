from typing import Union
from utils.load_data import load_data
from utils.write_data import write_data


# <------------------- GET FUNCTIONS ------------------->
def load_workout_data(workout: str, data: dict) -> Union[dict, None]:   # LOAD DATA OF ONE WORKOUT
    list_wrkts = data['workouts']

    for wrkt in list_wrkts:
        if wrkt['name'] == workout:
            return wrkt
    return None


def load_exercise_data(workout: str, exercise: str, data: dict) -> Union[dict, None]:   # LOAD DATA OF ONE EXERCISE
    wrkt_data = load_workout_data(workout, data)

    if wrkt_data is None:
        return None
    list_exs = wrkt_data['exercises']
    for exs in list_exs:
        if exs['name'] == exercise:
            return exs
    return None


def get_exercise_data(workout: str, exercise: str) -> dict:         # GET ALL DATA ABOUT ONE EXERCISE
    data = load_data()
    wrkt_data = load_workout_data(workout, data)
    exs_data = load_exercise_data(workout, exercise, data)

    if wrkt_data is None:
        return {
            "error": "Specified workout doesn't exist: " + workout,
            "data": {}
        }
    if exs_data is None:
        return {
            "error": "Specified exercise doesn't exist in selected workout: " + exercise,
            "data": {}
        }
    return {
        "error": "False",
        "workout": workout,
        "exercise": exercise,
        "data": exs_data
    }


def get_all_workouts() -> dict:                                     # GET LIST OF ALL WORKOUTS FROM DATA
    data = load_data()

    return {
        "error": "False",
        "data": data['workouts']
    }


def get_all_exercises(workout: str) -> dict:                        # GET LIST OF ALL EXERCISES IN SPECIFIED WORKOUT
    data = load_data()
    wrkt_data = load_workout_data(workout, data)

    if wrkt_data is None:
        return {
            "error": "Specified workout doesn't exist: " + workout,
            "data": {}
        }
    return {
        "error": "False",
        "workout": workout,
        "data": wrkt_data['exercises']
    }


def get_active_workout() -> dict:
    data = load_data()

    return data['active_workout']


# <------------------- PUT FUNCTIONS ------------------->
def put_new_workout(workout_name: str) -> dict:                     # PUT NEW WORKOUT INTO DATA
    return {
        "error": "False"
    }


def put_new_exercise(workout: str, exercise_name: str) -> dict:     # PUT NEW EXERCISE INTO WORKOUT
    return {
        "error": "False"
    }


def put_new_set(
        workout: str,
        xercise: str,
        weight: float,
        repetitions: int) -> dict:                                  # PUT NEW SET OF EXERCISE
    return {
        "error": "False"
    }
