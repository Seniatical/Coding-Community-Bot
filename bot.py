import discord
import json
import os
import re
import datetime
import traceback
import random
import asyncio
from discord.ext import commands
from pip._vendor import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

bot = commands.Bot(command_prefix = '>')
bot.remove_command('help')

@bot.event
async def on_member_join(member):
    acceptable_nick = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    final = []
    for x in range(5):
        keys = random.choice(acceptable_nick)
        final.append(keys)
    final2 = ''.join(final)
    for i in member.name:
        if i in acceptable_nick:
            return 
    await member.edit(nick = f"Moderated Nickname {final2}")
    embed = discord.Embed(title = 'Untaggable Username\n',
     description = 'We automatically detected that your username includes no normal english characters or symbols.\nAs a result your nickname was automatically set. You may ask any staff member to change your nickname for you.',
     color = discord.Colour.red())
    await member.send(embed = embed)
    userAvatarUrl = member.avatar_url   
    channel = bot.get_channel(743817386792058971)
    embed=discord.Embed(title=f'Hello welcome to the server {member}')
    embed.add_field(name='Account created at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    embed.add_field(name='Joined at:', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    embed.set_thumbnail(url=userAvatarUrl)    
    await channel.send(embed = embed)
    
@bot.event
async def on_member_update(before,after):
    acceptable_nick = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    final = []
    for x in range(5):
        keys = random.choice(acceptable_nick)
        final.append(keys)
    final2 = ''.join(final)
    for i in after.nick:
        if i in acceptable_nick:
            return 
    await after.edit(nick = f"Moderated Nickname {final2}")

@bot.command()
@commands.is_owner()
async def enable(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title = ':white_check_mark: **Successfully Enabled ' + extension + '.**')
    await ctx.send(embed = embed)

@bot.command()
@commands.is_owner()
async def disable(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(title = ':white_check_mark: **Successfully disabled ' + extension + '.**')
    await ctx.send(embed = embed)

@bot.command()
@commands.is_owner()
async def reload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title = ':white_check_mark: **Successfully reloaded ' + extension + '.**')
    await ctx.send(embed = embed)


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')
from itertools import cycle


client = commands.Bot(command_prefix = get_prefix)
status = cycle(['in 10000+ servers', 'with fire', 'with beer','the ban hammer'])

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
    change_status.start()
    print('<------------------------------>')
    print('Coding Comunity Bot is ready')
    print('<------------------------------>')

            
@help.command()
async def info(ctx):
            embed=discord.Embed(color=discord.Colour.orange())
            embed=discord.Embed(title=':information_source: info Commands :information_source:', description='\n\n`>whois` - sends the mentioned users info!!!\n`>avatar` - sends the mentioned persons PFP!!!\n`>info` - info about the bot!\n`>server` - info about the server.\n`>channelinfo` - info about the channel.\n>`suggest` - allow people to vote on your idea.')   
            await ctx.send(embed=embed)

@bot.command(aliases=['whois', 'userinfo'])
async def user(ctx, member: discord.Member):
  roles = [role for role in member.roles]
  embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())
  embed.set_author(name=f"{member}", icon_url=member.avatar_url)
  embed.set_thumbnail(url=member.avatar_url)
  embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))
  embed.add_field(name='Registered at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p'))
  embed.add_field(name='Bot?', value=f'{member.bot}')
  embed.add_field(name='Status?', value=f'{member.status}')
  embed.add_field(name='Top Role?', value=f'{member.top_role}')
  embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
  embed.set_footer(icon_url=member.avatar_url, text=f'Requested By: {ctx.author.name}')
  await ctx.send(embed=embed)


    
@bot.command()
@commands.has_permissions(manage_guild=True)
async def warn(ctx , member : discord.Member ,* , reason = "No reason Provided"):
  with open('warnings.json','r') as f:
    warns = json.load(f)
  if str(ctx.guild.id) not in warns:
    warns[str(ctx.guild.id)] = {}
  if str(member.id) not in warns[str(ctx.guild.id)]:
    warns[str(ctx.guild.id)][str(member.id)] = {}
    warns[str(ctx.guild.id)][str(member.id)]["warns"] = 1
    warns[str(ctx.guild.id)][str(member.id)]["warnings"] = [reason]
  else:
    warns[str(ctx.guild.id)][str(member.id)]["warnings"].append(reason)
  with open('warnings.json','w') as f:
    json.dump(warns , f)
    await ctx.send(f"{member.mention} was warned for: {reason}")
    
    embed = discord.Embed(title='You have been warned in The Coding Community', description=f'You received a warning from {member}')
    embed.add_field(name='Reason:', value=f'{reason}')
    await member.send(embed=embed)
    
@bot.command()
@commands.has_permissions(manage_guild=True)
async def removewarn(ctx, member: discord.Member, num: int, *, reason='No reason provided.'):
  with open('warnings.json' , 'r') as f:
    warns = json.load(f)
  num -= 1
  warns[str(ctx.guild.id)][str(member.id)]["warns"] -= 1
  warns[str(ctx.guild.id)][str(member.id)]["warnings"].pop(num)
  with open('warnings.json' , 'w') as f:
    json.dump(warns , f)
    await ctx.send('Warn has been removed!')
    embed = discord.Embed(title='Your warn in The Coding Community has been removed', description=f'Your warning was removed by {ctx.author}')
    await member.send(embed=embed)

        
@bot.command()
@commands.has_permissions(manage_guild=True)
async def warns(ctx , member : discord.Member):
  with open('warnings.json', 'r') as f:
    warns = json.load(f)
  num = 1
  warnings = discord.Embed(title = f"{member}\'s warns")
  for warn in warns[str(ctx.guild.id)][str(member.id)]["warnings"]:
    warnings.add_field(name = f"Warn {num}" , value = warn)
    num += 1
  await ctx.send(embed = warnings)

@bot.command()
async def verify(ctx):
        try:
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
            if code.isnumeric() == True:
                print('Nope')
            else:
                img = Image.new('RGB', (360, 180), color = 'white')

                d = ImageDraw.Draw(img)
                font = ImageFont.truetype("Futura.ttf", 90)
                d.text((3, 9.2), f"{code}", font=font, fill=(0,0,0))
                img.save('back.png')


            embed = discord.Embed(title='Type the code below to get verified!')
            embed.set_image(url="attachment://back.png")
            image = discord.File("back.png")
            await member.send(embed=embed, file=image)
            ctx.guild = None
            if ctx.guild == None:
                await asyncio.sleep(5)
                print('made it 1')
                def check(x):
                    return x.author == ctx.author
                print('made it 2')
                verif = await bot.wait_for('message',check = check, timeout = 300)
                print(verif)
                if verif.content == code:
                    await member.send('You passed the verification process!')
                else:
                    await member.send('You failed the verification process!\nTry again!')
        except Exception:
            traceback.print_exc()

@bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.CheckFailure):
    embed = discord.Embed(title = ':x:You do not have permission to use this command.', color = discord.Colour.red())
    await ctx.send(embed = embed)
  elif isinstance(error,commands.MissingRequiredArgument):
    embed = discord.Embed(title = ':x:You are missing the required arguements. Please check if your command requires an addition arguement.', color = discord.Colour.red())
    await ctx.send(embed = embed)
  elif isinstance(error, commands.CommandNotFound):
    pass
  elif isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title = ':x:Woah too fast there! This Command is on Cooldown!', color = discord.Colour.red())
    await ctx.send(embed = embed)

            
@bot.command(aliases=['thx', 'THX', 'thankyou'])
async def thank(ctx,member:discord.Member):
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


@bot.command(aliases=['thxlb'])
async def thxleaderboard(ctx,x=10):
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

@bot.command()
async def checkthanks(ctx, member : discord.Member):
  with open('thank.json') as f:
    thank = json.load(f)
  total_thanks = thank[str(member.id)]['tpoin']
  embed = discord.Embed(
    title = "{}'s total thanks!".format(member),
    colour = discord.Colour.red(),
    description = "The user currently has {} thanks.".format(total_thanks))
  embed.set_footer(text=f'User ID: {member.id}')
  await ctx.send(embed=embed)


bot.run('TOKEN')
