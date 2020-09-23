import discord
import asyncio
from discord.ext import commands

class Dalek(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    async def beer(self, ctx, user: discord.Member = None, reason: commands.clean_content = ""):

        if not user or user.id == ctx.author.id:
            return await ctx.send(f"{ctx.author.name}: paaaarty!:tada::beer:")
        if user.id == self.bot.user.id:
            return await ctx.send("drinks beer with you* :beers:")
        if user.bot:
            return await ctx.send(f"lol {ctx.author.name}lol")

        beer_offer = f"{user.name}, you got a :beer: offer from {ctx.author.name}"
        beer_offer = beer_offer + f"\n\nReason: {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == ":beers:":
                return True
            return False

        try:
            await msg.add_reaction(":beers:")
            await self.bot.wait_for('raw_reaction_add', timeout=30.0, check=reaction_check)
            await msg.edit(content=f"{user.name} and {ctx.author.name} are enjoying a lovely beer together :beers:")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"well, doesn't seem like {user.name} wanted a beer with you {ctx.author.name} ;-;")
        except discord.Forbidden:
            beer_offer = f"{user.name}, you got a :beer: from {ctx.author.name}"
            beer_offer = beer_offer + f"\n\nReason: {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)
        
    @commands.command()
    async def amiadmin(self,ctx):
        if ctx.author.guild_permissions.administrator == True:
            await ctx.send(f'Yes {ctx.author.name} you are an admin! :white_check_mark:')
        elif ctx.author.id == 579326961038524446:
            await ctx.send('Yes Happy Days you are an admin! :white_check_mark:')
        else:
            await ctx.send(f'no, heck off {ctx.author.name}')
            
    @commands.command()
    async def dm(self, ctx, user_id: int, *, message: str):
        user = self.bot.get_user(user_id)
        if not user:
            return await ctx.send(f"Could not find any UserID matching {user_id}")

        try:
            await user.send(message)
            await ctx.send(f":envelope: Sent a DM to {user_id}")
        except discord.Forbidden:
            await ctx.send("This user might be having DMs blocked or it's a bot account...")
            
    @commands.command()
    async def dalekping(self, ctx):
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send(":ping_pong: Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f":ping_pong: WS: {before_ws}ms  |  REST: {int(ping)}ms")
            
def setup(bot):
    bot.add_cog(Dalek(bot))
