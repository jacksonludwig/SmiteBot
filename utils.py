import json


def get_token():
    with open("token.json") as file:
        data = json.load(file)
        return data["token"]


def log_messages(message):
    # log messages
    print('Message from {0.author}: {0.content}'.format(message))