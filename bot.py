import utils
import scrape_data
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print("Smite bot is now running...")


@client.command()
async def scrape(context, god_name, game_mode):
    await context.send(scrape_data.get_page_info(god_name, game_mode))


@client.event
async def on_message(message):
    utils.log_messages(message)

    if message.author == client.user:
        return

    await client.process_commands(message)


def main():
    client.run(utils.get_token())


main()
