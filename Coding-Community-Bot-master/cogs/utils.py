import discord
import time
import math
import json
import random
import datetime
import traceback
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
        self.left_members = []

    @tasks.loop(seconds = 180)
    async def resetcount(self):
        self.count = 0

    @commands.Cog.listener()
    async def on_ready(self):
        self.resetcount.start()

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        self.left_members.append(member)

    @commands.Cog.listener()
    async def on_member_join(self,member):
        a = member.joined_at
        b = member.created_at
        c = a - b
        d = c.total_seconds()
        time = display_time(d)
        embed = discord.Embed(title = str(member) + " Suspicion evaluation: ")

        sus = "No"
        suspoints = 0

        date = d/60
        date = int(date)
        if date > 30240:
            pass
        else:
            suspoints += 3
            embed.add_field(name = "Member's account is less than a month old.", value = 'Failed Created At Test +3')
        if member.avatar_url == member.default_avatar_url:
            embed.add_field(name = "Member failed PFP test", value = 'Failed PFP test. +2')
            suspoints += 2

        bad = False

        acceptable_nick = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' '] 
        for i in member.name:
            if i in acceptable_nick:
                pass
            else:
                bad = True
                embed.add_field(name = "Member has a name with unacceptable characters.", value = 'Unacceptable Nickname. +2')
                break
        if bad == True:
            suspoints += 2

        bans = await member.guild.bans()
        ban_search = False

        for x in bans:
            if member in bans and x.id != member.id:
                ban_search = True
        if ban_search == True:
            suspoints += 2
            embed.add_field(name = "Suspected impersonation of banned user",value = 'Banned name Suspicion +2')

        imp = False

        for x in member.guild.members:
            found_ident = member.guild.get_member_named(member.name)
            if found_ident != member:
                imp = True
        if imp == True:
            suspoints += 3
            embed.add_field(name = 'Impersonating a current user.', value = 'Impersonation of User +3')


        list_bad = ['fuck','shit','cunt','slut','motherfucker','dick']
        if member.name in list_bad:
            suspoints += 5
            embed.add_field(name = 'User has bad word in name', value = 'Bad Word in Name +5')

        if member in self.left_members:
            suspoints += 2
            embed.add_field(name = "User left and rejoined", value = 'Left and rejoined +2')

        embed.set_footer(text = f'Total Score: {suspoints}')

        modapprove = False

        if suspoints > 8:
            sus = "Yes"
            embed.add_field(name = "Final result: ", value = f"{member} requires Moderator approval.")
        elif suspoints > 4 and suspoints < 8:
            sus = "Maybe"
            embed.add_field(name = "Final result: ", value = f"{member} requires Captcha.")
        

        channel = self.bot.get_channel(743817386792058971)
        channel2 = self.bot.get_channel(764615732905902101)

        await channel2.send(embed = embed)
        await channel.send(f"Welcome to The Coding Academy, {member.mention} <a:blobjump:729741013295431701> \n➥ Suspicious Account: {sus} <a:moneyspeed:726841128867070023> \n➥ Account made {time} ago <a:wumpuskey:726842149869584465>")
        if member.id == 719088658627559444:
            await channel.send(f"Congratulations! You are our {len(member.guild.members)}th member! As such, you can have free admin. Just ping Swas.py.")

    @commands.command()
    async def verify(self,ctx):
        try:
            if ctx.message.channel.id == 759220767711297566 or ctx.message.channel.id == 759159713870643281:
                await ctx.message.delete()
            mem = discord.utils.get(ctx.guild.roles, name = 'Member')
            if mem in ctx.author.roles:
                return
            needcap = False
            a = ctx.author.joined_at
            b = ctx.author.created_at
            c = a - b
            d = c.total_seconds()
            time = display_time(d)

            sus = "No"
            suspoints = 0

            print(str(ctx.author) + "'s Verification Results")
            date = d/60
            date = int(date)
            if date > 30240:
                pass
            else:
                print('Failed Created At Test +3')
                suspoints += 3
            if ctx.author.avatar_url == ctx.author.default_avatar_url:
                print('Failed PFP test. +2')
                suspoints += 2

            bad = False

            acceptable_nick = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' '] 
            for i in ctx.author.name:
                if i in acceptable_nick:
                    pass
                else:
                    bad = True
            if bad == True:
                print('Unacceptable Nickname. +2')
                suspoints += 2

            bans = await ctx.guild.bans()
            ban_search = False

            for x in bans:
                if ctx.author in bans and x.id != ctx.author.id:
                    ban_search = True
            if ban_search == True:
                print('Banned name Suspicion +2')
                suspoints += 2

            imp = False

            for x in ctx.guild.members:
                found_ident = ctx.guild.get_member_named(ctx.author.name)
                if found_ident != ctx.author:
                    imp = True
            if imp == True:
                print('Impersonation of User +3')
                suspoints += 3


            list_bad = ['fuck','shit','cunt','slut','motherfucker','dick']
            if ctx.author.name in list_bad:
                print('Bad Word in Name +5')
                suspoints += 5

            if ctx.author in self.left_members:
                print('Left and rejoined +2')
                suspoints += 2

            print(f'Total Score: {suspoints}')

            modapprove = False

            if suspoints > 8:
                sus = "Yes"
                modapprove = True
                print('Needs Moderator Approval')
            elif suspoints > 4 and suspoints < 8:
                sus = "Maybe"
                needcap = True
                print('Needs Captcha')

            if modapprove == True:
                embed = discord.Embed(title = "Your account has been flagged for suspicious behavior.", description = 'To get verified, please ping a mod to review your case.')
                await ctx.author.send(embed = embed)
            elif self.count == 5 or needcap == True:
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
                        embedf = discord.Embed(title = 'Incorrect Captcha, please request a new Captcha by redoing the ">verify" command in #verify-here')
                        await member.send(embed = embedf)
                except asyncio.TimeoutError:
                    embedt = discord.Embed(title = 'You have timed out, please run >verify again.')
                    await member.send(embed = embedt)
            else:
                role = discord.utils.get(ctx.guild.roles, name = 'Member')
                await ctx.author.add_roles(role)
                rem = discord.utils.get(ctx.guild.roles, name = 'Unverified')
                await ctx.author.remove_roles(rem)
                self.count += 1
        except discord.Forbidden:
            msg2 = await ctx.send(f"{ctx.author.mention}")
            embedd = discord.Embed(title = f"{ctx.author}, I had trouble contacting you, please make sure your DM's are open.")
            msg = await ctx.send(embed = embedd)
            await asyncio.sleep(15)
            await msg.delete()
            await msg2.delete()
        except Exception as e:
            traceback.print_exc()

    
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
            member = self.bot.get_user(id_)
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

    @commands.command()
    async def remind(self,ctx,time,*,reminder):
        try:
            indicator = time[-1]
            if not time[:-1].isnumeric():
                await ctx.send("Please provide a valid time.")
                return
            time = int(time[:-1])
            if time * 3600 > 21600 and indicator == 'h' or time * 60 > 21600 and indicator == 'm' or time > 21600 and indicator == 's':
                embed = discord.Embed(title = "We cannot set a reminder for more than 6 hours due to the amount of times the bot has to reboot.")
                await ctx.send(embed = embed)
                return
            embed = discord.Embed(title = 'Reminder Set!:white_check_mark:', color = discord.Colour.blurple())
            embed.add_field(name = f"{ctx.author}, succesfully set a reminder which will end in {time}{indicator}.", value = 'I will remind you when the timer is up!')
            await ctx.send(embed = embed)
            if indicator == 'm':
                await asyncio.sleep(int(time) * 60)
            elif indicator == 'h':
                await asyncio.sleep(int(time) * 3600)
            elif indicator == 's':
                await asyncio.sleep(int(time))
            await ctx.send(ctx.author.mention)
            em = discord.Embed(title = "Reminder! ", description = reminder, color = discord.Colour.green())
            await ctx.send(embed = em)
        except Exception as e:
            print(e)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def afk(self,ctx):
        helper = ctx.guild.get_role(726650418444107869)

        if not helper in ctx.author.roles:
            await ctx.send("Only Helpers can use this for now!")
            return 

        on_patrol = ctx.guild.get_role(760844827804958730)

        await ctx.author.remove_roles(on_patrol)

        await ctx.send(ctx.author.mention + ", you are AFK now!")

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.channel.id == 759220767711297566:
            await msg.delete()
            return
        helper = msg.guild.get_role(726650418444107869)

        if helper in msg.author.roles:

            on_patrol = msg.guild.get_role(760844827804958730)

            if not on_patrol in msg.author.roles:
                if msg.channel.id == 754710893538836480 or msg.channel.id == 754710998769991680 or msg.channel.id == 754711103665078273 or msg.channel.id == 7762722440853192746 or msg.channel.id == 762722834861523045 and msg.author.bot == False:

                    await msg.author.add_roles(on_patrol)

                    await msg.channel.send(msg.author.mention + ", your AFK was removed since you are on duty!")

    @commands.command(aliases = ["removecooldown","uncool","coolno"])
    @commands.has_permissions(manage_messages = True)
    async def remcool(self,ctx, member:discord.Member):
        cool = discord.utils.get(ctx.guild.roles, name = 'Cooldown')
        await member.remove_roles(cool)
        await ctx.send(f"The cooldown role has been removed from {member}")

    @commands.command()
    async def og(self,ctx,amt:int):
        all = {}
        for member in ctx.guild.members:
            pos = sum(m.joined_at < member.joined_at for m in ctx.guild.members if m.joined_at is not None)
            all[pos] = member

        embed = discord.Embed(title = f"First {amt} people to join!", color = discord.Colour.red())

        ratelimitew = ""

        for i in range(int(amt)):
            ratelimitew += (str(i) + "." + all[i].name) + "\n"
            embed.add_field(name =f"Number {i}:", value = all[i].mention,inline = False)

        await ctx.send(embed = embed)

    @commands.command()
    async def joined(self,ctx,posi:int):
        all = {}
        for member in ctx.guild.members:
            pos = sum(m.joined_at < member.joined_at for m in ctx.guild.members if m.joined_at is not None)
            all[pos] = member
        embed = discord.Embed(title = f"The {posi}th person to join is: ", description = all[posi].mention, color = discord.Colour.green())
        await ctx.send(embed = embed)
                        
def setup(bot):
    bot.add_cog(Utility(bot))
