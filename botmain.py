import discord
from discord.ext import commands

from bs4 import BeautifulSoup

import datetime
from ruamel.yaml import YAML

import os

from google.cloud import translate_v2 as translate

yaml = YAML()

# config file load in
with open('./config.yml', 'r', encoding = 'utf-8') as file:
    config = yaml.load(file)

# bot access
bot = commands.Bot(command_prefix = config['Prefix'])
key = os.getenv(config['Bot Key'])
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv(config['Api Key'])
bot.load_extension('COGS.management')

# !help command
@bot.command()
async def aider(ctx):
    await ctx.send('Coucou, mon ami ! Je m\'appelle Monsieur et je suis ton bot personnel. Ne t\'inquiète pas, pour je suis ici pour t\'aider avec les translations' +
                    ' entre tous les choses anglais et français.\n\n!french + word: Pour traduire en français.\n!english + word: Pour traduire en anglais.')

# !french command
@bot.command()
@commands.has_role('bulbasoir')
async def french(ctx, *, text):
    translate_client = translate.Client()
    target = 'fr'
    result = translate_client.translate(
        text,
        target_language = target
    )
    soup = BeautifulSoup(result['translatedText'], 'html.parser')
    await ctx.send('FR: {}'.format(soup))

# !english command
@bot.command()
async def english(ctx, *, text):
    translate_client = translate.Client()
    target = 'en'
    result = translate_client.translate(
        text,
        target_language = target
    )
    soup = BeautifulSoup(result['translatedText'], 'html.parser')
    await ctx.send(u'EN: {}'.format(result['translatedText']))

# !restart command
@bot.command(name = 'restart', aliases = ['r'], help = 'Restarts this bot.')
@commands.has_role('bulbasoir')
async def restart(ctx):
    await ctx.send("Redémarrer en cours . . .")
    await bot.close()



bot.run(key, bot = True)