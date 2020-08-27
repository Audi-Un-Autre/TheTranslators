import asyncio

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
bot2 = commands.Bot(command_prefix = config['Prefix'])
key = os.getenv(config['Bot Key'])
key2 = os.getenv(config['Bot2 Key'])
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv(config['Api Key'])
bot.load_extension('COGS.management')
bot.load_extension('COGS.french')
bot2.load_extension('COGS.korean')
bot2.load_extension('COGS.management')

# !restart command
@bot.command()
@commands.has_role('bulbasoir')
async def restart(ctx):
    await ctx.send("Redémarrer en cours . . .")
    #await bot.close()
    loop.stop()

# run both french and korean bots
loop = asyncio.get_event_loop()
machine1 = loop.create_task(bot.start(key))
machine2 = loop.create_task(bot2.start(key2))
try:
    loop.run_forever()
finally:
    loop.stop()