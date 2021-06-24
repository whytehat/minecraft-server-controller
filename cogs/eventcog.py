from discord.ext import commands
import discord

class EventHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() 
    async def on_ready(self):
        print('||||Ready to controll servers||||')

    @commands.Cog.listener() 
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('please send all required arguments')

def setup(client):
    client.add_cog(EventHandler(client))