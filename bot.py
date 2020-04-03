import utils
import scrape_data
import discord
from discord.ext import commands

CONST_PRO_MARKER = "PRO"
CONST_START_SEPEARATOR = "SEPARATOR"

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print("Smite bot is now running...")


@client.command()
async def build(context, god_name, game_mode):
    data = scrape_data.get_results(god_name, game_mode)
    if data[0] == CONST_PRO_MARKER:
        embed1 = utils.make_pro_embed_start(data, CONST_START_SEPEARATOR)
        embed2 = utils.make_pro_embed_end(data)
        await context.send(embed=embed1)
        await context.send(embed=embed2)

  #  await context.send(embed=embed)
  #  await context.send(embed=embed2)


@client.event
async def on_message(message):
    utils.log_messages(message)

    if message.author == client.user:
        return

    await client.process_commands(message)


def main():
    client.run(utils.get_token())


main()
