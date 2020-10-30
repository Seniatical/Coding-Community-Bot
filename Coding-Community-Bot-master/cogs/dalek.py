import discord
import asyncio
import time
import random
import traceback
from discord.ext import commands

class Dalek(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    async def beer(self, ctx, user: discord.Member = None,*, reason: commands.clean_content = ""):
        try:
            if not user or user.id == ctx.author.id:
                return await ctx.send(f"{ctx.author.name}: paaaarty!:tada::beer:")
            if user.id == self.bot.user.id:
                return await ctx.send("drinks beer with you* :beers:")
            if user.bot:
                return await ctx.send(f"lol {ctx.author.name}lol")

            beer_offer = f"{user.name}, you got a :beer: offer from {ctx.author.name}"
            beer_offer = beer_offer + f"\n\nReason: {reason}" if reason else beer_offer
            msg = await ctx.send(beer_offer)

            def reaction_check(reaction, m):
                return m.id == user.id and str(reaction.emoji) == "🍻"

            try:
                await msg.add_reaction("🍻")
                await self.bot.wait_for('reaction_add', timeout=30.0, check=reaction_check)
                await msg.edit(content=f"{user.name} and {ctx.author.name} are enjoying a lovely beer together :beers:")
            except asyncio.TimeoutError:
                await msg.delete()
                await ctx.send(f"well, doesn't seem like {user.name} wanted a beer with you {ctx.author.name} ;-;")
            except discord.Forbidden:
                beer_offer = f"{user.name}, you got a :beer: from {ctx.author.name}"
                beer_offer = beer_offer + f"\n\nReason: {reason}" if reason else beer_offer
                await msg.edit(content=beer_offer)
        except Exception:
            traceback.print_exc()
        
    @commands.command()
    async def amiadmin(self,ctx):
        if ctx.author.guild_permissions.administrator == True:
            await ctx.send(f'Yes {ctx.author.name} you are an admin! :white_check_mark:')
        elif ctx.author.id == 579326961038524446:
            await ctx.send('Yes Happy Days you are an admin! :white_check_mark:')
        else:
            await ctx.send(f'no, heck off {ctx.author.name}')
            
    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send(":ping_pong: Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f":ping_pong: WS: {before_ws}ms  |  REST: {int(ping)}ms")

    @commands.command(aliases=['howhot', 'hot'])
    async def hotcalc(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = ":broken_heart:"
        if hot > 25:
            emoji = ":heart:"
        if hot > 50:
            emoji = ":sparkling_heart:"
        if hot > 75:
            emoji = ":revolving_hearts:"

        await ctx.send(f"{user.name} is {hot:.2f}% hot {emoji}")
            
def setup(bot):
    bot.add_cog(Dalek(bot))
