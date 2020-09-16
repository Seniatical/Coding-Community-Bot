import discord
import traceback
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client


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
            em = discord.Embed(title = 'Please specify a member.',colour = discord.Colour.orange())
            em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
            await ctx.send(embed = em)
            return
        await member.ban(reason = reason)
        em = discord.Embed(title = f'You banned {member}',colour = discord.Colour.orange())
        em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
        await ctx.send(embed = em)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            em = discord.Embed(title = 'Nice try but you are not allowed to ban people',colour = discord.Colour.orange())
            em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
            await ctx.send(embed = em)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                em = discord.Embed(title = f'You Unbanned {user.mention}',colour = discord.Colour.orange())
                em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
                await ctx.send(embed = em)
                return            

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            em = discord.Embed(title = 'Nice try but you are not allowed to unban people',colour = discord.Colour.orange())
            em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
            await ctx.send(embed = em)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member:discord.Member = None):
        if not member:
            em = discord.Embed(title = 'Please specify a member.',colour = discord.Colour.orange())
            em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
            await ctx.send(embed = em)
            return
        await member.kick()
        em = discord.Embed(title = f'You kicked {member}',colour = discord.Colour.orange())
        em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
        await ctx.send(embed = em)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            em = discord.Embed(title = 'Nice try but you are not allowed to kick people',colour = discord.Colour.orange())
            em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
            await ctx.send(embed = em)

    #mute command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member=None):
        if not member:
            em = discord.Embed(title = 'Please specify a member.',colour = discord.Colour.orange())
            em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
            await ctx.send(embed = em)
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        em = discord.Embed(title = f'{member.mention} got Got muted',colour = discord.Colour.orange())
        em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
        await ctx.send(embed = em)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            em = discord.Embed(title = 'Nice try but you are not allowed to mute people',colour = discord.Colour.orange())
            em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
            await ctx.send(embed = em)

    #unmute command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member=None):
        if not member:
            em = discord.Embed(title = 'Please specify a member.',colour = discord.Colour.orange())
            em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
            await ctx.send(embed = em)
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        em = discord.Embed(title = f'{member.mention} got unmuted',colour = discord.Colour.orange())
        em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
        await ctx.send(embed = em)
    @mute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            em = discord.Embed(title = 'Nice try but you are not allowed to unmute people',colour = discord.Colour.orange())
            em.set_footer(text="Coded by daftscientist#8570 | CereBro | User ID: " + str(ctx.message.author.id))
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(Mod(client))