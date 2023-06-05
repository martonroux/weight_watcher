from utils.import_utils import *
from data_manager.body_weight_data import get_body_weight_data
from fastapi import HTTPException


def get_body_weight(app):
    @app.get("/api/get/body_weight/all_data")                           # GET FULL BODY WEIGHT DATA
    def get_data():
        data = get_body_weight_data()
        if data['error'] != "False":
            raise HTTPException(                                        # ERROR IF GET_BODY_WEIGHT_DATA RETURNS ERROR
                status_code=400,
                detail=data['error']
            )
        list_weight = data['list']

        return {
            "errors": "False",
            "data": {
                "list": list_weight,
                "average": get_average(list_weight),
                "evolution": get_evolution(list_weight),
                "median": get_median(list_weight)
            }
        }
