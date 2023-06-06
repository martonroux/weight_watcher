from utils.load_data import load_data


def get_body_weight_data() -> dict:
    data = load_data()
    return {
        "error": "False",
        "list": data['bodyweight']['list']
    }
