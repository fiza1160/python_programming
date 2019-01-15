import argparse
import os
import tempfile
import json


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="storage entry key")
    parser.add_argument("--value", help="the value you want to add")
    return parser.parse_args()


def initialize_file(storage_path):
    if not os.path.exists(storage_path):
        with open(storage_path, 'w') as f:
            json.dump({}, f)


def read_storage(storage_path):
    with open(storage_path, 'r') as f:
        return json.load(f)


def found_values(storage_path, key):
    storage_data = read_storage(storage_path)
    if key in storage_data:
        print(*storage_data[key], sep=', ')
    else:
        print(None)


def add_new_value(storage_path, key, value):
    storage_data = read_storage(storage_path)
    if key in storage_data:
        storage_data[key].append(value)
    else:
        storage_data[key] = [value]
    with open(storage_path, 'w') as f:
        json.dump(storage_data, f, sort_keys=True)


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    initialize_file(storage_path)

    args = parse_command_line()
    if args.value is None:
        found_values(storage_path, args.key)
    else:
        add_new_value(storage_path, args.key, args.value)
