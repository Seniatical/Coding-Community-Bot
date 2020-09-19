import discord
import traceback
import random
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

  #help command
  @commands.command()
  async def help(self, ctx):
              embed=discord.Embed(title='Bot Commands', description='\n\n`>helpmod` :hammer_pick: ➣ For moderation commands\n`>helpfun` :zany_face: ➣ For Epic fun commands\n`>helpinfo` :information_source: ➣ For infomation commands\n`>helpmusic` ➣ For the music commands\n`>helputils` ➣ For random utility commands\n`>helprandom` ➣ for random commands that dont fit in.')
              await ctx.send(embed=embed)

  @commands.command()
  async def helpmusic(self, ctx):
              embed=discord.Embed()
              embed=discord.Embed(title=':musical_note: Music Commands! :musical_note:', description='\n\n`>play` - plays a song\n`>queue` - shows the guilds queue\n`>remove` - removes a song from a guilds queue\n`>skip` - skips a song from the guilds queue\n`>songinfo` - shows info on the song you are playing\n`>stop` - stops the player\n`>fskip` - force skips the song\n`>fremove` - force removes a song from the queue')
              await ctx.send(embed=embed)

  @commands.command()
  async def helpmod(self, ctx):
              embed=discord.Embed(title=':hammer_pick: Moderation Commands :hammer_pick:', description='\n\n`>clear` - This command clears a spesified  ammount of messages from a text channel\n`>mute` - Mutes the spesified player\n`>unmute` - This command unmutes a user.\n`>kick` - Kicks a spesified user\n`>ban` - This command bans a user.\n`>unban` - This command bans a user.\n`>lockdown` - This locksdown a certain channel.\n`>warn` - This warns the user. \n`>removewarn` - This removes a warn.\n`>warns` - This shows warns.\n`>lock` - locks a channel\n`>unlock` - unlocks a channel\n`>slowmode` - sets channel slowmode')
              await ctx.send(embed=embed)

  #fun help command
  @commands.command()
  async def helpfun(self, ctx):
              embed=discord.Embed(title=':zany_face: Fun Commands :zany_face:', description='\n\n`>8ball` - This command you say _8ball then ask your question!\n`>whisper` - lets you send a dm to someone.\n`>camel` - lets you camelfy a word!\n`>reverse` - lets you reverse a word!\n`>password` - generates you a random password\n`>sayname` - says the users name!')
              await ctx.send(embed=embed)
   
   @commands.command()
   async def helputils(self, ctx)
              embed=discord.Embed(title='coming soon!')
              await ctx.send(embed=embed)
   
   
   @commands.command()
   async def helprandom(self, ctx)
              embed=discord.Embed(title='coming soon!')
              await ctx.send(embed=embed)
   

    @commands.command()
    async def helpcurrency(ctx):
                embed=discord.Embed(color=discord.Colour.orange())
                embed=discord.Embed(title=':money_with_wings: Currency Commands :money_with_wings:', description='\n\n`?bag` - Shows you your inventory\n`?balance` - Shows you your balence!\n`?beg` - lets you ask for money!\n`?work` - lets work for money!\n`?buy` - lets you buy somthing!\n`?dep` - lets you put money from wallet to bank!\n`?rob` - lets you steal from someone!\n`?send` - lets you send someone money\n`?shop` - lets you see availible products\n`?slots` - lets you gamble\n`?with` - lets you take money from bank and put it in wallet!\n`?leaderboard` - lets see the highest people!\n`?sell` - lets you sell an object!')
                await ctx.send(embed=embed)
   
 



