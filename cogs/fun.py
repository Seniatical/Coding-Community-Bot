import discord
import traceback
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['mock','laugh','drunk','drunkify'])
    async def camel(self,ctx,*,msg):
        msg = list(msg)
        converted = []
        for x in msg:
            try:
                qt = random.randint(0,1)
                if qt == 1:
                    convert = x.upper()
                    converted.append(convert)
                elif qt == 0:
                    convert = x.lower()
                    converted.append(convert)
            except:
                pass

        final = ''.join(converted)
        await ctx.send(final)
        
    @commands.command()
    async def reverse(self,ctx,*,msg):
        try:
            msg = list(msg)
            msg.reverse()
            print(msg)
            send = ''.join(msg)
            await ctx.send(send)
        except Exception:
            traceback.print_exc()
            
    @commands.command(aliases = ['pass','generator','password','passwordgenerator'])
    async def _pass(self,ctx,amt : int = 8):
        try:
            nwpss = []
            lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z','!','@',
            '#','$','%','^','&','*','(',')','-','_','+','=','{',",",'}',']',
            '[',';',':','<','>','?','/','1','2','3','4','5','6','7','8','9','0'
            ,'`','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
            ,'Q','R','S','T','U','V','W','X','Y','Z']
            for x in range(amt):
                newpass = random.choice(lst)
                nwpss.append(newpass)
            fnpss = ''.join(nwpss)

            await ctx.send(f'{ctx.author} attempting to send you the genereated password in dms.')
            await ctx.author.send(f':white_check_mark:Password Generated: {fnpss}')
        except Exception as e:
            print(e)
            
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
    async def count(self,ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        messages = await channel.history(limit=None).flatten()
        count = len(messages)
        embed = discord.Embed(
            title="Total Messages",
            colour=0x2859b8,
        description=f"There were {count} messages in {channel.mention}")
        await ctx.send(embed=embed)






def setup(bot):
    bot.add_cog(Fun(bot))
