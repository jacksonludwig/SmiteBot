import json
import discord
from discord.ext import commands

sep_index = 0


def get_token():
    with open("token.json") as file:
        data = json.load(file)
        return data["token"]


def log_messages(message):
    print('Message from {0.author}: {0.content}'.format(message))


def make_pro_embed_start(data, CONST_START_SEPEARATOR):
    embed = discord.Embed(
        title="Starting build",
        color=discord.Color.blue()
    )
    global sep_index
    for i in range(1, len(data)):
        if data[i] == CONST_START_SEPEARATOR:
            sep_index = i
            break
        embed.add_field(name="{}.)".format(
            i), value=data[i], inline=False)

    return embed


def make_pro_embed_end(data):
    embed = discord.Embed(
        title="Ending build",
        color=discord.Color.blue()
    )
    global sep_index
    for i in range(sep_index + 1, len(data)):
        embed.add_field(name="{}.)".format(
            i - sep_index), value=data[i], inline=False)

    return embed
