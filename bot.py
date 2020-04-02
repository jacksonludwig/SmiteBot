import load_token
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="$")


def log_messages(message):
    # log messages
    print('Message from {0.author}: {0.content}'.format(message))


@client.event
async def on_ready():
    print("Smite bot is now running...")


@client.event
async def on_message(message):
    log_messages(message)

    if message.author == client.user:
        return


def main():
    client.run(load_token.get_token())


main()
