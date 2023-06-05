# <------------------- GET FUNCTIONS ------------------->


def get_exercise_data(workout: str, exercise: str) -> dict:         # GET ALL DATA ABOUT ONE EXERCISE
    if workout is not "Pecs":
        return {
            "error": "Specified workout doesn't exist: " + workout,
            "data": {}
        }
    if exercise is not "bench press":
        return {
            "error": "Specified exercise doesn't exist in selected workout: " + exercise,
            "data": {}
        }
    return {
        "error": "False",
        "workout": workout,
        "exercise": exercise,
        "list": []
    }


def get_all_workouts() -> dict:                                     # GET LIST OF ALL WORKOUTS FROM DATA
    return {
        "error": "False",
        "list": [
            "Pecs"
        ]
    }


def get_all_exercises(workout: str) -> dict:                        # GET LIST OF ALL EXERCISES IN SPECIFIED WORKOUT
    if workout is not "Pecs":
        return {
            "error": "Specified workout doesn't exist: " + workout,
            "data": {}
        }
    return {
        "error": "False",
        "workout": workout,
        "list": [
            "bench press"
        ]
    }


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
