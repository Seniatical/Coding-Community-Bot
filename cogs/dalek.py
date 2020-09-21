import discord
from discord.ext import commands

class Dalek(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    async def amiadmin(self,ctx):
        if ctx.author.guild_permissions.administrator == True:
            await ctx.send(f'Yes {ctx.author.name} you are an admin! :white_check_mark:')
        elif ctx.author.id == 579326961038524446:
            await ctx.send('Yes Happy Days you are an admin! :white_check_mark:')
        else:
            await ctx.send(f'no, heck off {ctx.author.name}')
            
def setup(bot):
    bot.add_cog(Dalek(bot))
