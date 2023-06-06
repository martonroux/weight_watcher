import json


def write_data(data: dict) -> None:
    with open('data.json', 'r') as fd:
        json.dump(data, fd, indent=2)
