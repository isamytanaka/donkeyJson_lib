import json

def load_json(path: str):
    """Loads the content of a JSON file."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"The file {path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding the JSON in {path}.")
        return None

def save_json(path: str, data: dict):
    """Saves a dictionary as a JSON file."""
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving the JSON file: {e}")

def add_data_json(path: str, new_data: dict):
    """Loads the JSON file, adds new data, and saves it again."""
    current_data = load_json(path)
    if current_data is not None:
        current_data.update(new_data)
        save_json(path, current_data)