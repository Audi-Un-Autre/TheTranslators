# This cog listens to all command calls and reports error directly to the user in the channel

import discord
from discord.ext import commands

from botmain import config

class ErrorHandling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # General error response
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        errorFormat = self.bot.get_cog('Formatting')
        if isinstance(error, commands.CommandNotFound):
            await errorFormat.formatGeneral(ctx, 'Command not recognized.')
        if isinstance(error, commands.CheckFailure):
            await errorFormat.formatGeneral(ctx, 'You do not have permission to do this.')
        if isinstance(error, commands.BadArgument):
            await errorFormat.formatGeneral(ctx, 'Invalid argument. Command canceled.')
        if isinstance(error, commands.MissingRequiredArgument):
            await errorFormat.formatGeneral(ctx, 'Nothing to translate. Please retry in the format of: ```!french + word``````!english + word```')
        if isinstance(error, discord.Forbidden):
            await errorFormat.formatGeneral(ctx, 'I don\'t have permission to do this.')
    

def setup(bot):
    bot.add_cog(ErrorHandling(bot))