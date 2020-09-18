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
        
    @commands.command(aliases = ['info'])
    async def whois(self,ctx, member:discord.Member):
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(title = str(member) + "'s profile:", description = 'Requested by: ' + str(ctx.author),color = discord.Colour.from_rgb(54,151,255))
        embed.set_image(url = str(member.avatar_url))
        embed.add_field(name = 'Member joined guild on:', value = str(member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC")), inline = True)
        embed.add_field(name = 'Member joined discord on:', value = str(member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")),inline = True)
        embed.add_field(name = "Member's nickname:", value = str(member.nick))
        embed.add_field(name = "Member's roles: ", value=" ".join([role.mention for role in roles]), inline = True)
        embed.add_field(name = "Member's top role:", value = str(member.top_role.mention),inline = True)
        embed.add_field(name = "Member's id:", value = str(member.id))
        await ctx.send(embed = embed)

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






def setup(bot):
    bot.add_cog(Info(bot))
