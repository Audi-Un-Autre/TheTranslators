import discord
from discord.ext import commands

from ruamel.yaml import YAML

yaml = YAML()

# config file load in
with open('./config.yml', 'r', encoding = 'utf-8') as file:
    config = yaml.load(file)

class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # notice of online
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Management cog is active on ' + self.bot.user.name)
        print(self.bot.user.name + f' is now online.')
        await self.bot.change_presence(status = discord.Status.idle, activity = discord.Game(config['Playing Status']))
        await self.bot.get_channel(config['Log Channel ID']).send(self.bot.user.name + ' is now online.')
    
    @commands.Cog.listener()
    # member join notice
    async def on_member_join(self, member):
        await self.bot.get_channel(config['Log Channel ID']).send(f'{member} has joined the server.')
        await self.bot.get_channel(config['Main Channel ID']).send(f'Greetings, {member} !')

    # member leave notice
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.bot.get_channel(config['Log Channel ID']).send(f'{member} has left the server.')
        await self.bot.get_channel(config['Main Channel ID']).send(f'A shame, {member} has left the server.')

    # kick
    @commands.command()
    @commands.has_role('bulbasoir')
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.invoke(self.bot.get_command('clearchat'), query = 1)
        await ctx.send(member + ' has been removed from the server. Reason : ' + reason)
        await member.kick(reason=reason)

    # ban
    @commands.command()
    @commands.has_role('bulbasoir')
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.invoke(self.bot.get_command('clearchat'), query = 1)
        await ctx.send(member + ' has been banned from the server. Reason : ' + reason)
        await member.ban(reason=reason)

    # !clearchat
    @commands.command()
    @commands.has_role('bulbasoir')
    async def clearchat(self, ctx, amount:int):
        if amount > 100 or amount <= 0:
            await ctx.send('Error : Please enter a number between 1 - 100.')
        else:
            deleted = await ctx.channel.purge(limit = amount)
            await ctx.send('{} messages have been removed.'.format(len(deleted)))

def setup(bot):
    bot.add_cog(Management(bot))