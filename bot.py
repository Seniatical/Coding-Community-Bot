import discord
import json
import os
import re
import datetime
import traceback
import random
from itertools import cycle
import asyncio
from discord.ext import commands, tasks
from pip._vendor import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

bot = commands.Bot(command_prefix = 'not ', case_insensitive=True, intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_connect():
    print('Connected to Discord')

class NotSwas(Exception):
	pass

def IsSwas():
	async def predicate(ctx):
		if ctx.author.id != 556119013298667520:
			raise NotSwas('This is person is not swas.')
		return True
	commands.check(predicate)

@bot.event
async def on_member_join(member):
    try:
        unv = discord.utils.get(member.guild.roles, name = 'Unverified')
        await member.add_roles(unv)
        mod = True
        acceptable_nick = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        final = []
        for x in range(5):
            keys = random.choice(acceptable_nick)
            final.append(keys)
        final2 = ''.join(final)
        for i in member.name:
            if i in acceptable_nick:
                mod = False
        if mod == True:
            await member.edit(nick = f"Moderated Nickname {final2}")
            embed = discord.Embed(title = 'Untaggable Username\n',
            description = 'We automatically detected that your username includes no normal english characters or symbols.\nAs a result your nickname was automatically set. You may ask any staff member to change your nickname for you.',
            color = discord.Colour.red())
            await member.send(embed = embed)
    except:
        pass
        
@bot.event
async def on_member_update(before,after):
    try:
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
    except:
        pass

@bot.command()
@IsSwas()
async def enable(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title = ':white_check_mark: **Successfully Enabled ' + extension + '.**')
    await ctx.send(embed = embed)

@bot.command()
@IsSwas()
async def disable(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(title = ':white_check_mark: **Successfully disabled ' + extension + '.**')
    await ctx.send(embed = embed)

@bot.command()
@IsSwas()
async def reload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title = ':white_check_mark: **Successfully reloaded ' + extension + '.**')
    await ctx.send(embed = embed)


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')

status = cycle(['in 10000+ servers', 'with fire', 'with beer','the ban hammer'])

@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.command()
async def party(ctx):
	await ctx.send('<a:partycat:728839448757796865>')    
    
    
    
@bot.event
async def on_ready():
    change_status.start()
    print('<------------------------------>')
    print('Coding Comunity Bot is ready')
    print(f'Using Discord.py Version {discord.__version__}')
    print('<------------------------------>')

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
  elif isinstance(error, NotSwas):
	await ctx.send('Your not Swas.py#7370!')

bot.run('TOKEN')

