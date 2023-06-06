import json


def load_data() -> dict:
    with open('data.json', 'r') as fd:
        data = json.load(fd)
    return data
