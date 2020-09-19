import discord
import traceback
import random
from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        embed=discord.Embed(title=f'{avamember} avatar!!')
        embed.set_image(url=userAvatarUrl)
        await ctx.send(embed=embed)


    @commands.command(aliases = ['guild'])
    async def server(self, ctx):
            findbots = sum(1 for member in ctx.guild.members if member.bot)
            embed = discord.Embed(title = 'Infomation about ' + ctx.guild.name + '.', colour = discord.Colour.from_rgb(54,151,255))
            embed.set_thumbnail(url = str(ctx.guild.icon_url))
            embed.add_field(name = "Guild's name: ", value = ctx.guild.name)
            embed.add_field(name = "Guild's owner: ", value = str(ctx.guild.owner))
            embed.add_field(name = "Guild's verification level: ", value = str(ctx.guild.verification_level))
            embed.add_field(name = "Guild's id: ", value = str(ctx.guild.id))
            embed.add_field(name = "Guild's member count: ", value = str(ctx.guild.member_count))
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name = "Guild created at: ", value = str(ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
            await ctx.send(embed =  embed)
            
    @commands.command(aliases=['idea', 'tell', 'suggestion'])
    async def suggest(self, ctx, *, suggestion = None):
        channel = bot.get_channel(729711188392280154)
        if suggestion == None:
            await ctx.send('Please follow this format:\n`>suggest **Your suggestion**`')
        else:
            em = discord.Embed(title=f'Suggestion by {ctx.author.name}', description=suggestion, color=discord.Color(0xf58742))
            em.set_footer(text='Have an idea? use `>suggest` in a bot command channel!')
            await ctx.message.delete()
            msg = channel.send(embed=em)
            msg.add_reaction('\U00002705')
            msg.add_reaction('\u274E')



def setup(bot):
    bot.add_cog(Info(bot))
