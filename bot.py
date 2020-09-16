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



@bot.command()
@commands.has_permissions(administrator = True)
async def enable(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title = ':white_check_mark: **Successfully Enabled ' + extension + '.**')
    await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(administrator = True)
async def disable(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(title = ':white_check_mark: **Successfully disabled ' + extension + '.**')
    await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(administrator = True)
async def reload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title = ':white_check_mark: **Successfully reloaded ' + extension + '.**')
    await ctx.send(embed = embed)


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Watching(name="General Chat!"))
    print('<------------------------------>')
    print('Coding Comunity Bot is ready')
    print('<------------------------------>')




has_avatar = commands.check(lambda ctx: ctx.avatar_url != ctx.author.default_avatar_url)

@has_avatar
@bot.event
async def on_member_join(member):
        try:
            alpha = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
            numeric = ('1','2','3','4','5','6','7','8','9','0')
            final = []

            member = member
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
            if member.id == None:
                await asyncio.sleep(5)
                print('made it 1')
                def check(x):
                    return x.author == member
                print('made it 2')
                verif = await bot_two.wait_for('message',check = check, timeout = 300)
                print(verif)
                if verif.content == code:
                    await member.send('You passed the verification process!')
                else:
                    await member.send('You failed the verification process!\nTry again!')
        except Exception:
            traceback.print_exc()


@bot.command()
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
    
    embed = discord.Embed(title='You have been warned in The Coding Community', description=f'You received a warning from {ctx.author}')
    embed.add_field(name='Reason:', value=f'{reason}')
    await member.send(embed=embed)
    
@bot.command()
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
                verif = await bot_two.wait_for('message',check = check, timeout = 300)
                print(verif)
                if verif.content == code:
                    await member.send('You passed the verification process!')
                else:
                    await member.send('You failed the verification process!\nTry again!')
        except Exception:
            traceback.print_exc()

            
#help command
bot.remove_command('help')
@bot.group()
async def help(ctx):
    if ctx.invoked_subcommand is None:
            embed=discord.Embed()
            embed=discord.Embed(title='Bot Commands', description='\n\n`?help mod` :hammer_pick: ➣ For moderation commands\n`?help fun` :zany_face: ➣ For Epic fun commands\n`?help currency` :money_with_wings: ➣ For currency commands\n`?help info` :information_source: ➣ For infomation commands\n`?help music` ➣ For the music commands')
            await ctx.send(embed=embed)

@help.command()
async def music(ctx):
            embed=discord.Embed()
#            embed=discord.Embed(title=':musical_note: Music Commands! :musical_note:', description='\n\n`?play` - plays a song\n`?queue` - shows the guilds queue\n`?remove` - removes a song from a guilds queue\n`?skip` - skips a song from the guilds queue\n`?songinfo` - shows info on the song you are playing\n`?stop` - stops the player\n`?fskip` - force skips the song\n`?fremove` - force removes a song from the queue')
            embed=discord.Embed(title=':musical_note: Music Commands coming soon!:musical_note:')
            await ctx.send(embed=embed)

@help.command()
async def mod(ctx):
            embed=discord.Embed()
            embed=discord.Embed(title=':hammer_pick: Moderation Commands :hammer_pick:', description='\n\n`?clear` - This command clears a spesified  ammount of messages from a text channel\n`?mute` - Mutes the spesified player\n`?unmute` - This command unmutes a user.\n`?kick` - Kicks a spesified user\n`?ban` - This command bans a user.\n`?unban` - This command bans a user.\n`?lockdown` - This locksdown a certain channel.\n`?warn` - This warns the user. \n`?removewarn` - This removes a warn.\n`?warns` - This shows warns. ')
            await ctx.send(embed=embed)

#fun help command
@help.command()
async def fun(ctx):
            embed=discord.Embed(color=discord.Colour.orange())
#            embed=discord.Embed(title=':zany_face: Fun Commands :zany_face:', description='\n\n`?8ball` - This command you say _8ball then ask your question!\n`?ping` - Lets you play ping pong with the bot!\n`?whisper` - lets you send a dm to someone.')
            embed=discord.Embed(title=':zany_face: Fun Commands coming soon! :zany_face:'
            await ctx.send(embed=embed)
            
@help.command()
async def info(ctx):
            embed=discord.Embed(color=discord.Colour.orange())
            embed=discord.Embed(title=':information_source: info Commands :information_source:', description='\n\n`?whois` - sends the mentioned users info!!!\n`?avatar` - sends the mentioned persons PFP!!!\n`?info` - info about the bot!\n`?server` - info about the server.\n`?channelinfo` - info about the channel.')   
            await ctx.send(embed=embed)
            
            
@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title='',color=discord.Color.red())
    if isinstance(error, commands.BadArgument):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name='Invalid Permissions', value=f'You dont have {error.missing_perms} permissions')
        await ctx.send(embed=embed)
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.CommandOnCooldown):
        if error.retry_after < 60:
            f=round(error.retry_after) / 60
            embed.add_field(name=f'Your on cooldown!', value=f'Stop trying. Wait {round(error.retry_after, 0)} seconds and retry again.')
            await ctx.send(embed=embed)
    if isinstance(error, commands.ArgumentParsingError):
        pass
    if isinstance(error, commands.BadUnionArgument):
        pass
            
bot.run('')
