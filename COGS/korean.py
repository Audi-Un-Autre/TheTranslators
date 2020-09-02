# This cog will handle all Korean commands

import discord
from discord.ext import commands

from bs4 import BeautifulSoup

from google.cloud import translate_v2 as translate

from botmain import config, restrict

class Korean(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Korean Cog is active.')
        greeting = self.bot.user.name + '은 이제 온라인 상태입니다.'
        await self.bot.get_cog('Formatting').formatGeneral(self.bot.get_channel(config['Korean Channel ID']), greeting)
        await self.bot.change_presence(status = discord.Status.online, activity = discord.Game(config['K Playing Status']))

    # !help command
    @commands.command()
    async def doum(self, ctx):
        commandInfo = ('오 안녕하세요. 뭔가 필요하세요? 봐, 할 일이있어. 내 서비스가 필요하면 입력하여 도움을 요청하십시오.')
        await self.bot.get_cog('Formatting').formatGeneral(ctx, commandInfo)

    # !french command
    @commands.command()
    @commands.has_role(restrict)
    async def korean(self, ctx, *, text):
        translate_client = translate.Client()
        target = 'ko'
        result = translate_client.translate(
            text,
            target_language = target
        )
        soup = BeautifulSoup(result['translatedText'], 'html.parser')
        await self.bot.get_cog('Formatting').formatTranslation(text, soup, ctx)

    # !english command
    @commands.command()
    @commands.has_role(restrict)
    async def english(self, ctx, *, text):
        translate_client = translate.Client()
        target = 'en'
        result = translate_client.translate(
            text,
            target_language = target
        )
        soup = BeautifulSoup(result['translatedText'], 'html.parser')
        await self.bot.get_cog('Formatting').formatTranslation(text, soup, ctx)

def setup(bot):
    bot.add_cog(Korean(bot))