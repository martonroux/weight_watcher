import json


def write_data(data: dict) -> None:
    with open('data.json', 'w') as fd:
        json.dump(data, fd, indent=2)
