import json

def load_data():
    filepath = input('Укажите путь к файлу:')
    with open(filepath, 'r') as json_file:
        return json.load(json_file)

def pretty_print_json(data):
    return print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii = False))

if __name__ == '__main__':
    pretty_print_json(load_data())