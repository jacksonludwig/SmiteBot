import json
import discord


def get_token():
    with open("token.json") as file:
        data = json.load(file)
        return data["token"]


class Client(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.author == self.user:
            return
        if message.content == "ping":
            await message.channel.send("pong")


def main():
    client = Client()
    client.run(get_token())


main()
