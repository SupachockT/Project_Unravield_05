import json


def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{file_path}': {e}")
    except Exception as e:
        print(f"An error occurred while loading data from '{file_path}': {e}")
    return None


def update_data(json_file, data):
    try:
        with open(json_file, "w") as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error updating data: {e}")


def update_money(data, uid, new_money):
    if uid in data:
        data[uid]["money"] = new_money
        return True
    else:
        return False
