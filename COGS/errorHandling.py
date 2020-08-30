import discord
from discord.ext import commands

from botmain import config

class ErrorHandling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        errormsg = 'Command not recognized.'
        errorFormat = self.bot.get_cog('Formatting')
        if isinstance(error, commands.CommandNotFound):
            await errorFormat.formatGeneral(ctx, errormsg)
            
    
    #@commands.french.error
    #async def french_error(self, ctx, error):
    #    if isinstance(error, commands.MissingRequiredArgument):
    #        await ctx.send()


def setup(bot):
    bot.add_cog(ErrorHandling(bot))