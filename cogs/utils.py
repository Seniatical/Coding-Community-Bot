import discord
import time
import math
import json
import random
import asyncio
from captcha.image import ImageCaptcha
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from discord.ext import commands, tasks

intervals = (
    ('years', 604800*52),
    ('months', 604800*4),
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
    )


def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            value = round(value)
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

class Utility(commands.Cog):
    
    def __init__ (self,bot):
        self.bot = bot
        self.count = 0

    @tasks.loop(seconds = 180)
    async def resetcount(self):
        self.count = 0

    @commands.Cog.listener()
    async def on_ready(self):
        self.resetcount.start()

    @commands.command()
    async def ping(self, ctx):
        em = discord.Embed(title='Latency', description='Pong {0}'.format(math.trunc(bot.latency * 1000)) + 'ms', color=discord.Color(0x4293f5))
        await ctx.send(embed=em)

    @commands.Cog.listener()
    async def on_member_join(self,member):
        a = member.joined_at
        b = member.created_at
        c = a - b
        d = c.total_seconds()
        time = display_time(d)

        sus = "No"

        t_sus = 1-(d/604800)
        print(t_sus)
        if member.avatar_url == member.default_avatar_url:
            t_sus+=0.4

        if t_sus>0.8:
            sus = "Yes"
            giverole = discord.utils.get(member.guild.roles, name = 'sus')
            await member.add_roles(giverole)
        elif t_sus>0.375:
            sus = "Maybe"
        

        channel = self.bot.get_channel(743817386792058971)

        await channel.send(f"Welcome to The Coding Academy, {member.mention} <:blobjump:729741013295431701> \n➥ Suspicious Account: {sus} <:moneyspeed:726841128867070023> \n➥ Account made {time} ago <:wumpuskey:726842149869584465>")
        if member.id == 719088658627559444:
            await channel.send(f"Congratulations! You are our {len(member.guild.members)}th member! As such, you can have free admin. Just ping Swas.py.")

    @commands.command()
    async def verify(self,ctx):
        try:
            needcap = False
            a = ctx.author.joined_at
            b = ctx.author.created_at
            c = a - b
            d = c.total_seconds()
            time = display_time(d)

            sus = "No"

            t_sus = 1-(d/604800)
            print(t_sus)
            if ctx.author.avatar_url == ctx.author.default_avatar_url:
                t_sus+=0.4

            if t_sus>0.8:
                sus = "Yes"
                needcap = True
            elif t_sus>0.375:
                sus = "Maybe"
            mem = discord.utils.get(ctx.guild.roles, name = 'Member')
            if mem in ctx.author.roles:
                return
            if self.count == 10 or needcap == True:
                alpha = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
                numeric = ('1','2','3','4','5','6','7','8','9','0')
                final = []

                member = ctx.author
                for i in range(6):
                    des = ('alpha', 'numeric')
                    an = random.choice(des)
                    if an == 'alpha':
                        a = random.choice(alpha)
                        cap = ('lower', 'upper')
                        caps = random.choice(cap)
                        if caps == 'lower':
                            final.append(a.lower())
                        else:
                            final.append(a.upper())
                    else:
                        a = random.choice(numeric)
                        final.append(a)
                code = ''.join(map(str, final))
                image = ImageCaptcha()
                data = image.generate(code)
                image.write(code, 'back.png')

                try:
                    embed = discord.Embed(title = 'Captcha')
                    embed.add_field(name= 'To prevent spam bots from coming into our server, please verify by solving this Captcha',
                        value = 'Please Type the Below Code into this Dm.')
                    embed.set_image(url="attachment://back.png")
                    image = discord.File("back.png")
                    await member.send(embed=embed, file=image)
                    await asyncio.sleep(5) 
                    print(code)
                    def check(x):
                        return x.author == ctx.author and x.guild == None
                    verif = await self.bot.wait_for('message',check = check, timeout = 300)
                    if verif.content == code:
                        embeda = discord.Embed(title = 'You passed the verification process and was given access to the rest of the server.')
                        await member.send(embed = embeda)
                        role = discord.utils.get(ctx.guild.roles, name = 'Member')
                        await ctx.author.add_roles(role)
                        rem = discord.utils.get(ctx.guild.roles, name = 'Unverified')
                        await ctx.author.remove_roles(rem)
                    else:
                        embedf = discord.Embed(title = 'You failed the verification process, please try again.')
                        await member.send(embed = embedf)
                except discord.Forbidden:
                    embedd = discord.Embed(title = f"{ctx.author} I had trouble contacting you, please make sure your DM's are open.")
                    await ctx.send(embed = embedd)
                except asyncio.TimeoutError:
                    embedt = discord.Embed(title = 'You have timed out, please run >verify again.')
                    await member.send(embed = embedt)
            else:
                role = discord.utils.get(ctx.guild.roles, name = 'Member')
                await ctx.author.add_roles(role)
                rem = discord.utils.get(ctx.guild.roles, name = 'Unverified')
                await ctx.author.remove_roles(rem)
                self.count += 1
        except Exception as e:
            print(e)

    
    @commands.command()
    async def create(self,ctx, name, *,thing):
        with open('tag.json','r') as f:
            tag = json.load(f)
        if str(ctx.guild.id) not in tag:
            tag[str(ctx.guild.id)] = {}
            tag[str(ctx.guild.id)]['tags'] = []
            with open('tag.json','w') as f:
                json.dump(tag,f)
            with open('tag.json','w') as f:
                json.dump(tag,f)
        
        tagies = None

        for tags in tag[str(ctx.guild.id)]['tags']:
            tagies = tags['tag']

        if name == tagies:
            return False
            
        else:
            a = {'tag':name,'info':thing,'author':ctx.author.id}
            tag[str(ctx.guild.id)]['tags'].append(a)
            with open('tag.json','w') as f:
                json.dump(tag,f)
            with open('tag.json','w') as f:
                json.dump(tag,f)
            await ctx.send(f'Success! Tag {name} created!')


    @commands.command()
    async def tag(self,ctx,name):
        with open('tag.json','r') as f:
            tag = json.load(f)
        if str(ctx.guild.id) not in tag:
            tag[str(ctx.guild.id)] = {}
            tag[str(ctx.guild.id)]['tags'] = []
            with open('tag.json','w') as f:
                json.dump(tag,f)
        
        tagies = None
        info = None

        for tags in tag[str(ctx.guild.id)]['tags']:
            tagies = tags['tag']
            info = tags['info']
        
        if tagies == name:
            await ctx.send(info)
        else:
            await ctx.send('No Tag found.')
            return False

    @commands.command(aliases=['thx', 'THX', 'thankyou'])
    async def thank(self,ctx,member:discord.Member):
        if member == ctx.author:
            return False
        elif ctx.author.bot:
            return False
        with open('thank.json','r') as f:
            thank = json.load(f)
        if str(member.id) not in thank:
            thank[str(member.id)] = {}
            thank[str(member.id)]['tpoin'] = 1

        else:
            thank[str(member.id)]['tpoin'] += 1

        with open("thank.json","w") as f:
            json.dump(thank,f)
        await ctx.send(f'You have thanked {member}')


    @commands.command(aliases=['thxlb'])
    async def thxleaderboard(self,ctx, x=10):
        with open('thank.json') as f:
            thank = json.load(f)
        leaderb = {}
        total = []
        for user in thank:
            name = int(user)
            
            total_amt = thank[user]['tpoin']

            leaderb[total_amt] = name
            total.append(total_amt)
        
        total = sorted(total,reverse=True)
        index = 1

        em = discord.Embed(title=f'Top {x}', color=random.randint(0,0xFFFFF))

        for amt in total:
            check = []
            id_ = leaderb[amt]
            member = bot.get_user(id_)
            name = member.name
            id = member.id
        if id in check:
            pass
        else:
            em.add_field(name=f'{index}. {name}',value=f"Points : `{amt}` | ID: `{id}`",inline=False)
            check.append(id)
            index += 1
        await ctx.send(embed=em)

    @commands.command()
    async def checkthanks(self,ctx, member : discord.Member):
        with open('thank.json') as f:
            thank = json.load(f)
        total_thanks = thank[str(member.id)]['tpoin']
        embed = discord.Embed(
            title = "{}'s total thanks!".format(member),
            colour = discord.Colour.red(),
            description = "The user currently has {} thanks.".format(total_thanks))
        embed.set_footer(text=f'User ID: {member.id}')
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title = 'This command is on Cooldown, please wait {:.2f}s or ping a staff member before trying to verify again.'.format(error.retry_after),
             color = discord.Colour.red())
            await ctx.send(embed = embed)
                    
def setup(bot):
    bot.add_cog(Utility(bot))
