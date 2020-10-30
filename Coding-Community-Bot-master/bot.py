import discord
import json
import os
import re
import datetime
import traceback
import random
import sys
from itertools import cycle
import asyncio
from discord.ext import commands, tasks
from pip._vendor import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

bot = commands.Bot(command_prefix = '>')
bot.remove_command('help')

@bot.event
async def on_connect():
    print('Connected to Discord')

@bot.event
async def on_member_join(member):
    try:
        mod = True
        acceptable_nick = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
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
        acceptable_nick = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
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

bot.unload_extension("cogs.mail")
bot.unload_extension("cogs.ticket")
bot.unload_extension("cogs.help")

@bot.command()
async def credits(ctx):
    embed = discord.Embed(title = "Credits: ", description = "These people helped make Coding Bot Possible.", color = discord.Colour.green())
    embed.add_field(name = 'Swas.py', value = "He is what really made Coding Bot possible, his videos attracted the attention of people who helped make Coding Bot a thing.")
    embed.add_field(name = "Happy Days", value = "Hosting, he helped host Coding Bot with 64GB of Ram and 20TB of Storage.")
    embed.add_field(name = "daftscientist", value = "He was actually the first person to think up of this idea, he had the idea where we can revive the old Coding Bot in a new bot!")
    embed.set_footer(text = "I'm bored 10/10/20")
    await ctx.send(embed = embed)

status = cycle(['in 10000+ servers', 'with fire', 'with beer','the ban hammer'])

@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
    change_status.start()
    print('<------------------------------>')
    print('Coding Comunity Bot is ready')
    print(f'Using Discord.py Version {discord.__version__}')
    print('<------------------------------>')

@bot.command()
async def botkill(ctx):
    if ctx.author.id == 661717104914858038 or ctx.author.id == 401145022499520523 or ctx.author.id == 579326961038524446 or ctx.author.id == 556119013298667520:
        await ctx.send("Bot has been Successfully killed.")
        os.system("taskill /im py.exe")
        sys.exit(0)
    else:
        await ctx.send("You don't have permission to kill the bot.")

@bot.command()
async def reboot(ctx):
    await ctx.send("Rebooting...")
    sys.exit()

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

bot.run('')


