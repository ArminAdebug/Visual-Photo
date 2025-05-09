import json

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_from_json(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)
