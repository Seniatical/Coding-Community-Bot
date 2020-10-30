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

    
    @commands.command()
    async def helputils(self, ctx):
                embed=discord.Embed(title='utility commands!', description='\n\n`>checkthanks - checks a users thanks!\n `>thxlb` - lets you see the thanks leaderboard\n>thx - lets you thank a user')
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    
    



