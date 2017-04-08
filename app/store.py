import json
import writer
import reader

__user_list = []

DATA_FILE = 'user_data.json'


def add(user):
    __user_list.append(user)


def load():
    global __user_list
    # Read the stored data from the file.
    data = reader.read(DATA_FILE)
    # Deserialize the data from string.
    __user_list = json.loads(data)

    return __user_list


def save():
    # Convert the list of users to string (Serialize).
    data = json.dumps(__user_list)
    # Write the data to the file.
    writer.write(DATA_FILE, data)
