import discord
import traceback
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #8ball
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later."
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        em = discord.Embed(title = 'Magic 8ball!',colour = discord.Colour.orange())
        em.add_field(name=f"**Question:** {question}", value=f"**Answer:** {random.choice(responses)}")
        await ctx.send(embed = em)






    @commands.command()
    async def whisper(self, ctx, member : discord.Member, *,content):
            embed=discord.Embed(color=discord.Colour.orange())
            embed=discord.Embed(title='Someone Whispered To You!')
            embed.add_field(name='Message: '+ str(content), value="From"  + str(ctx.author.mention))
            await member.send(embed=embed)
            await ctx.message.delete()


    @commands.command()
    async def sayname(self, ctx, *,  avamember : discord.Member=None):
        await ctx.send(f"Your name is {ctx.author.mention}")



    @commands.command()
    async def count(ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        messages = await channel.history(limit=None).flatten()
        count = len(messages)
        embed = discord.Embed(
            title="Total Messages",
            colour=0x2859b8,
        description=f"There were {count} messages in {channel.mention}")
            await ctx.send(embed=embed)






def setup(client):
    client.add_cog(Fun(client))
