import discord
from discord.ext import commands

import datetime
from ruamel.yaml import YAML

import os

yaml = YAML()

# config file load in
with open('./config.yml', 'r', encoding = 'utf-8') as file:
    config = yaml.load(file)

# bot access
bot = commands.Bot(command_prefix = config['Prefix'])
key = os.getenv(config['Bot Key'])
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv(config['Api Key'])
bot.load_extension('COGS.management')
bot.load_extension('COGS.french')

# !restart command
@bot.command()
@commands.has_role('bulbasoir')
async def restart(ctx):
    await ctx.send("Redémarrer en cours . . .")
    await bot.close()

bot.run(key, bot = True)