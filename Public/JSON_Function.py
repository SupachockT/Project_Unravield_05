import json


def load_data(jsonFile):
    try:
        with open(jsonFile, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
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
