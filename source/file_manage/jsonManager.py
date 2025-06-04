import json
import os

module_dir = os.path.dirname(os.path.abspath(__file__))


def get_absolute_path(filename):

    if os.path.isabs(filename):
        return filename
    else:
        return os.path.join(module_dir, filename)


def save_to_json(data, filename):
    filename = get_absolute_path(filename)
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_from_json(filename):
    filename = get_absolute_path(filename)
    with open(filename, 'r') as json_file:
        return json.load(json_file)
