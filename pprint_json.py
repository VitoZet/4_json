import json

filepath = 'json_file.txt'

def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def pretty_print_json(json_data):
    return json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii = False)

if __name__ == '__main__':
    print(pretty_print_json(load_data(filepath)))
