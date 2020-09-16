import discord
import traceback
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # this is the clear command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx,amount=5):
        await ctx.channel.purge(limit=amount)

    #The below code bans player.
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member=None, *, reason = None):
        if member is None:
            em = discord.Embed(title = 'Please specify a member.')
            await ctx.send(embed = em)
            return
        await member.ban(reason = reason)
        em = discord.Embed(title = f'You banned {member}')
        await ctx.send(embed = em)
        
        embed = discord.Embed(title='You have been banned from The Coding Community', description=f'Banned by {member}')
        embed.add_field(name='Reason:', value=f'{reason}')
        await member.send(embed=embed)


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                em = discord.Embed(title = f'You Unbanned {user.mention}')
                await ctx.send(embed = em)
                return            



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member:discord.Member = None):
        if not member:
            em = discord.Embed(title = 'Please specify a member.')
            await ctx.send(embed = em)
            return
        await member.kick()
        em = discord.Embed(title = f'You kicked {member}')
        await ctx.send(embed = em)
        embed = discord.Embed(title='You have been kicked from The Coding Community', description=f'Kicked by {member}')
        embed.add_field(name='Reason:', value=f'{reason}')
        await member.send(embed=embed)


    #mute command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member=None):
        if not member:
            em = discord.Embed(title = 'Please specify a member.')
            await ctx.send(embed = em)
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        em = discord.Embed(title = f'You muted{member.mention}')
        await ctx.send(embed = em)
        embed = discord.Embed(title='You have been muted in The Coding Community', description=f'Muted by {member}')
        embed.add_field(name='Reason:', value=f'{reason}')
        await member.send(embed=embed)


    #unmute command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member=None):
        if not member:
            em = discord.Embed(title = 'Please specify a member.')
            await ctx.send(embed = em)
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        em = discord.Embed(title = f'{member.mention} got unmuted')
        await ctx.send(embed = em)
        embed = discord.Embed(title='You have been unmuted in The Coding Community', description=f'Unmuted by {member}')
        embed.add_field(name='Reason:', value=f'{reason}')
        await member.send(embed=embed)

def setup(bot):
    bot.add_cog(Mod(bot))
