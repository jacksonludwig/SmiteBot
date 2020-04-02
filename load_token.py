import json


def get_token():
    with open("token.json") as file:
        data = json.load(file)
        return data["token"]
