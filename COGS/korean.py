import discord
from discord.ext import commands

from bs4 import BeautifulSoup

from google.cloud import translate_v2 as translate

from botmain import config

class Korean(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Korean Cog is active.')
        await self.bot.get_channel(config['Korean Channel ID']).send(self.bot.user.name + '은 이제 온라인 상태입니다.')
        await self.bot.change_presence(status = discord.Status.online, activity = discord.Game(config['K Playing Status']))

    # !help command
    @commands.command()
    async def doum(self, ctx):
        await ctx.send('In Progress.')

    # !french command
    @commands.command()
    @commands.has_role('bulbasoir')
    async def korean(self, ctx, *, text):
        translate_client = translate.Client()
        target = 'ko'
        result = translate_client.translate(
            text,
            target_language = target
        )
        soup = BeautifulSoup(result['translatedText'], 'html.parser')
        await ctx.send('KO: {}'.format(soup))

    # !english command
    @commands.command()
    @commands.has_role('bulbasoir')
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
    bot.add_cog(Korean(bot))