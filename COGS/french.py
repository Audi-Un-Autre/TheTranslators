import discord
from discord.ext import commands

from bs4 import BeautifulSoup

from google.cloud import translate_v2 as translate

class French(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'French Cog is active.')

    # !help command
    @commands.command()
    async def aider(self, ctx):
        await ctx.send('Coucou, mon ami ! Je m\'appelle Monsieur et je suis ton bot personnel. ' +
                        'Ne t\'inquiète pas, pour je suis ici pour t\'aider avec les translations' +
                        ' entre tous les choses anglais et français.\n\n!french + word: Pour traduire en français.' +
                        '\n!english + word: Pour traduire en anglais.')

    # !french command
    @commands.command()
    @commands.has_role('bulbasoir')
    async def french(self, ctx, *, text):
        translate_client = translate.Client()
        target = 'fr'
        result = translate_client.translate(
            text,
            target_language = target
        )
        soup = BeautifulSoup(result['translatedText'], 'html.parser')
        await ctx.send('FR: {}'.format(soup))

    # !english command
    @commands.command()
    async def english(self, ctx, *, text):
        translate_client = translate.Client()
        target = 'en'
        result = translate_client.translate(
            text,
            target_language = target
        )
        soup = BeautifulSoup(result['translatedText'], 'html.parser')
        await ctx.send(u'EN: {}'.format(result['translatedText']))

def setup(bot):
    bot.add_cog(French(bot))