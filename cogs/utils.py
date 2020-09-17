import discord
import time
import math
from discord.ext import commands

class Utility(commands.Cog):
    
    def __init__ (self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        em = discord.Embed(title='Latency', description='Pong {0}'.format(math.trunc(bot.latency * 1000)) + 'ms', color=discord.Color(0x4293f5))
        await ctx.send(embed=em)
        
def setup(bot):
    bot.add_cog(Utility(bot))
