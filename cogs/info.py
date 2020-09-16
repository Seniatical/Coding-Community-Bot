import discord
import traceback
import random
from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client


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

    @commands.command(aliases = ['channelstats'])
    async def channelinfo(self, ctx,channel:discord.TextChannel):
            nsfw = self.get_channel(channel.id).is_nsfw()
            news = self.get_channel(channel.id).is_news()
            embed = discord.Embed(title = 'Channel Infomation: ' + str(channel), description = 'Channel Stats: ', 
            colour = discord.Colour.from_rgb(54, 151, 255))
            embed.add_field(name = 'Channel Name: ', value = str(channel.name))
            embed.add_field(name = "Channel's NSFW Status: ", value = str(nsfw))
            embed.add_field(name = "Channel's id: " , value = str(channel.id))
            embed.add_field(name = 'Channel Created At: ', value = str(channel.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
            embed.add_field(name = 'Channel Type: ', value = str(channel.type))
            embed.add_field(name = "Channel's Announcement Status: ", value = str(news))
            await ctx.send(embed = embed)




def setup(client):
    client.add_cog(Info(client))