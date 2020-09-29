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

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def lock(self,ctx, amount = 1):
        await ctx.channel.purge(limit = amount)
        await ctx.message.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(title = 'This channel has been locked by: ' + str(ctx.message.author))
        await ctx.send(embed=embed)
        
    @commands.command()
    async def nick(self,ctx,member:discord.Member,name):
        await member.edit(nick = name)
        embed = discord.Embed(title = 'Nick Name Successfully Changed!')
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def unlock(self,ctx, amount = 1):
        await ctx.channel.purge(limit = amount)
        await ctx.message.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(title = 'This channel has been unlocked by: ' + str(ctx.message.author))
        await ctx.send(embed=embed)

    @commands.command()
    async def slowmode(self,ctx,time:int):
        try:
            if time == 0:
                embed = discord.Embed(title = 'Slowmode turned off')
                await ctx.send(embed = embed)
                await ctx.channel.edit(slowmode_delay = 0)
            elif time > 21600:
                embed = discord.Embed(title = 'You cannot have a slowmode above 6hrs.')
                await ctx.send(embed = embed)
            else:
                await ctx.channel.edit(slowmode_delay = time)
                embed = discord.Embed(title = f'Slowmode set to {time} seconds.')
                await ctx.send(embed = embed)
        except Exception:
            traceback.print_exc()
            
        
    @commands.command()
    async def softban(self,ctx, member:discord.Member,*, reason = 'No reason provided'):
        await member.ban(reason = reason)
        await member.unban(reason = reason)
        embed = discord.Embed(title = f'Successfully softbanned {member}')
        await ctx.send(embed = embed)
    
    
    @commands.command()
    async def tempban(self,ctx,member:discord.Member,time,*,reason = 'No Reason Provided'):
        with open('guild.json','r') as f:
            channels = json.load(f)
        indicator = time[-1]
        if indicator == "m" or indicator == "s" or indicator == 'h' or indicator == 'd':
            pass
        else:
            await ctx.send('Incorrect Time Format.')
        embed = discord.Embed(title = f'{member} has been temp banned for {time}.')
        await ctx.send(embed = embed)
        await member.ban(reason = reason)
        chanid = channels[str(ctx.guild.id)]['admin'][0]['adid']
        channel = self.bot.get_channel(chanid)
        embed = discord.Embed(title = 'Member Tempbanned!', color = discord.Colour.red())
        embed.add_field(name = f'{member} was tempbanned({time}) from {ctx.guild.name} for: ',value = f'{reason}')
        await channel.send(embed = embed)
        time = time[:-1]
        if indicator == 'm':
            await asyncio.sleep(int(time) * 60)
        elif indicator == 'h':
            await asyncio.sleep(int(time) * 3600)
        elif indicator == 's':
            await asyncio.sleep(int(time))
        elif indicator == 'd':
            await asyncio.sleep(int(time) * 86400)
        await member.unban(reason = 'Timer has expired.')     

    @commands.command(aliases = ['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount:int = 5):
        await ctx.channel.purge(limit=amount)

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
    async def kick(self, ctx, member:discord.Member = None,*,reason = 'No reason provided'):
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

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def mute(self,ctx, member:discord.Member = None,time:str = None,*,reason = 'No reason provided'):
        try:
            while True:
                try:
                    if member == None:
                        em = discord.Embed(title = 'Please specify a member.')
                        await ctx.send(embed = em)
                        return
                    if member == ctx.message.author:
                        embed = discord.Embed(title = 'No you may not mute yourself.')
                        await ctx.send(embed = embed)
                        break
                    else:
                        indicator = time[-1]
                        if indicator == "m" or indicator == "s" or indicator == 'h' or indicator == 'd':
                            pass
                        else:
                            await ctx.send('Incorrect Time Format.')
                            break
                        muted_give = discord.utils.get(ctx.guild.roles, name = 'Muted')
                        await member.add_roles(muted_give)
                        embed = discord.Embed(title = str(member) + ' was successfully muted by: ' + str(ctx.author) + ' for ' + str(time) + ' Reason:' + str(reason))
                        await ctx.send(embed = embed)
                        time = time[:-1]
                        if indicator == 'm':
                            await asyncio.sleep(int(time) * 60)
                        elif indicator == 'h':
                            await asyncio.sleep(int(time) * 3600)
                        elif indicator == 's':
                            await asyncio.sleep(int(time))
                        elif indicator == 'd':
                            await asyncio.sleep(int(time) * 86400)
                        else: 
                            pass
                        await member.remove_roles(muted_give)
                        break
                except AttributeError:
                    muted = await ctx.guild.create_role(name = "Muted")
                    await ctx.message.channel.set_permissions(ctx.guild.get_role(muted.id), send_messages = False)
        except Exception:
            traceback.print_exc()

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def warn(self,ctx , member : discord.Member ,* , reason = "No reason Provided"):
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
            
            embed = discord.Embed(title='You have been warned in The Coding Community', description=f'You received a warning from {member}')
            embed.add_field(name='Reason:', value=f'{reason}')
            await member.send(embed=embed)
            
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def removewarn(self,ctx, member: discord.Member, num: int, *, reason='No reason provided.'):
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

            
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warns(self,ctx , member : discord.Member):
        with open('warnings.json', 'r') as f:
            warns = json.load(f)

        num = 1
        warnings = discord.Embed(title = f"{member}\'s warns")
        for warn in warns[str(ctx.guild.id)][str(member.id)]["warnings"]:
            warnings.add_field(name = f"Warn {num}" , value = warn)
            num += 1
        await ctx.send(embed = warnings)

def setup(bot):
    bot.add_cog(Mod(bot))
