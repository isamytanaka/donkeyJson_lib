## donkeyJson
**This library provides simple functions to load, save, and add data to JSON files. It's ideal for quick manipulation of JSON data, allowing efficient operations like reading, writing, and updating.**

## How to Use:

*1. Load a JSON file:*

Use `load_json(path)` to load data from a JSON file.


`data = load_json('file.json')`


*2. Save data to a JSON file:*

Use `save_json(path, data)` to save a dictionary as JSON in a file.


``data = {"name": "John", "age": 30}
save_json('file.json', data)``


*3. Add new data to an existing JSON file:*

Use `add_data_json(path, new_data)` to load a JSON file, add new data, and save it again.


``new_data = {"city": "São Paulo"}
add_data_json('file.json', new_data)``



**This library simplifies JSON data management with direct and easy-to-use functions.**

