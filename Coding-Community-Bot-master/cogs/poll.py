import discord
import asyncio
import traceback
import itertools
from discord.ext import commands, tasks

class Poll(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def poll(self,ctx):
        try:
            def check(x):
                return x.author == ctx.message.author and x.channel == ctx.message.channel

            embedtime = discord.Embed(title = "Setup: Step 1 out of 3", color = discord.Colour.green())
            embedtime.add_field(name = "Please provide the time the poll should last for.", value = "h = Hours\nm = Minutes\ns = Seconds\nd = Days")
            await ctx.send(embed = embedtime)
            try:
                time = await self.bot.wait_for('message',check = check, timeout = 60)
            except asyncio.TimeoutError:
                await ctx.send("**You have timed out please try again.**")
                return
            embedchoice = discord.Embed(title = "Setup: Step 2 out of 3", color = discord.Colour.green())
            embedchoice.add_field(name = "Please provide the amount of choices the poll will have.", value = "Please Provide a number not a Letter.")
            await ctx.send(embed = embedchoice)
            try:
                amount = await self.bot.wait_for('message', check = check, timeout = 60)
                amount = int(amount.content)
                if amount > 6:
                    await ctx.send("**You cannot have more than 5 choices.**")
                    return
                elif amount < 2:
                    await ctx.send("**Hey you cannot have les than 2 choices!**")
                    return
            except asyncio.TimeoutError:
                await ctx.send("**Timeout Error, please try again.**")
                return
            except TypeError:
                await ctx.send("**Please list a number not a letter.**")
                return
            embedid = discord.Embed(title = "Setup: Step 3 out of 3", color = discord.Colour.green())
            embedid.add_field(name = "Please provide the message id for the message the poll is going to run on.", value = "Please Provide a id.")
            await ctx.send(embed = embedid)
            try:
                msg_id = await self.bot.wait_for('message',check = check, timeout = 60)
                print(msg_id.content)
            except asyncio.TimeoutError:
                await ctx.send("**Timeout Error, please try again.**")
                return
            channel = self.bot.get_channel(764613122882666507)  
            message = await channel.fetch_message(int(msg_id.content))
            nums = ['🍞','✅','❌','📌','🍉','🔗']
            cyc = itertools.cycle(nums)
            for x in range(int(amount)):
                await message.add_reaction(next(cyc))

            indicator = time[:-1]
        except Exception:
            traceback.print_exc()

def setup(bot):
    bot.add_cog(Poll(bot))