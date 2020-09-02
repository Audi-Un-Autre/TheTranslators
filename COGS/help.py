# This cog overwrites the original Discord !help command
# Customised with expanded explanations of commands and formatting

import discord
from discord.ext import commands

from botmain import config

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print (f'Help Cog online.')

    # Show list of commands that this bot has
    @commands.command()
    async def help(self, ctx):
        commandList = []
        commandListAdmin = ['kick', 'ban', 'clearchat', 'restart']
        # Display to user only non-admin commands
        for command in self.bot.commands:
            if command.name in commandListAdmin:
                pass
            else:
                commandList.append(config['Prefix'] + command.name)
        await self.bot.get_cog('Formatting').formatGeneral(ctx, commandList)

def setup(bot):
    bot.add_cog(Help(bot))