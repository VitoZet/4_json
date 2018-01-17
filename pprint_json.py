import json

filepath = 'json_file.txt'

def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        return data

def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, indent=4, ensure_ascii = False)

if __name__ == '__main__':
    print(pretty_print_json(load_data(filepath)))