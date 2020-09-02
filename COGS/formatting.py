# This cog will format the bot's output before outputting to Discord

import discord
from discord.ext import commands

class Formatting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Formatting Cog online.')

    # Translation formatting
    @commands.Cog.listener()
    async def formatTranslation(self, request, result, ctx):
        embed = discord.Embed(
            title = self.bot.user.name + ' has recieved your request!',
            colour = discord.Colour.dark_purple()
        )

        embed.set_author(name = ctx.author.name, icon_url= ctx.author.avatar_url)
        embed.add_field(name = '\u200b', value = '\u200b', inline=False)
        embed.add_field(name = 'Your Request', value = request, inline=True)
        embed.add_field(name = 'Google Translation', value = result, inline=True)

        await ctx.send(embed=embed)

    # General non-translated formatting
    @commands.Cog.listener()
    async def formatGeneral(self, ctx, text):
        # if text is a list, parse out brackets, quotes, commas
        if isinstance(text, list):
            tempText = '\n'.join(str(x) for x in text)
            text = tempText
        embed = discord.Embed(
            color = discord.Colour.light_gray()
        )
        embed.add_field(name = 'System Message', value = text, inline = True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Formatting(bot))