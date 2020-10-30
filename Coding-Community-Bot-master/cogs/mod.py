import discord
import json
import os
import re
import datetime
import traceback
import random
import sys
import asyncio
from discord.ext import commands
from pip._vendor import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("@everyone") and message.author.id == 759126142875074580:
            await message.channel.send("Powering off, everyone or here ping exploit.")
            sys.exit()
        elif message.content.startswith("@here") and message.author.id == 7591261428750745801:
            await message.channel.send("Powering off, everyone or here ping exploit.")
            sys.exit()


    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def lock(self,ctx, amount = 1):
        await ctx.channel.purge(limit = amount)
        await ctx.message.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(title = 'This channel has been locked by: ' + str(ctx.message.author))
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def nick(self,ctx,member:discord.Member,*,name = None):
        if name == None:
            await member.edit(nick = ctx.author)
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
    @commands.has_permissions(manage_channels = True)
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
    @commands.has_permissions(ban_members = True)
    async def softban(self,ctx, member:discord.Member,*, reason = 'No reason provided'):
        await member.ban(reason = reason)
        await member.unban(reason = reason)
        embed = discord.Embed(title = f'Successfully softbanned {member}')
        await ctx.send(embed = embed)
    
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
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

    '''@commands.command()
    async def selfmute(self,ctx,time):
        try:
            orig_time = time
            embed = discord.Embed(title = f"Are you sure you want to mute yourself?", description =  f"Reacting will seriously mute you for {time}.\n If this is a mistake just do not react and wait for it to time out in 30 seconds.")
            msg = await ctx.send(embed = embed)
            def reactionchk(reaction,x):
                return x.id == ctx.author.id and str(reaction.emoji) == "👍"
            
            try:
                await msg.add_reaction("👍")
                await self.bot.wait_for('reaction_add', timeout = 30, check = reactionchk)
            except asyncio.TimeoutError:
                await ctx.send('Timeout Error, Aborting.')
            indicator = time[-1]
            if indicator == "m" or indicator == "s" or indicator == 'h':
                pass
                
            time = time[:-1]
            time = int(time)
            if time * 3600 > 21600 and indicator == 'h' or time * 60 > 21600 and indicator == 'm' or time > 21600 and indicator == 's':
                embed = discord.Embed(title = "We cannot mute you for more than 6 hours.")
                await ctx.send(embed = embed)
                return
            muted = discord.utils.get(ctx.guild.roles, name = 'Muted')
            await ctx.author.add_roles(muted)
            embed = discord.Embed(title = f'Successfully muted you for {orig_time}.')  
            await ctx.send(embed = embed)
            if indicator == 'm':
                await asyncio.sleep(int(time) * 60)
            elif indicator == 'h':
                await asyncio.sleep(int(time) * 3600)
            elif indicator == 's':
                await asyncio.sleep(int(time))
            await ctx.author.remove_roles(muted)
        except Exception:
            traceback.print_exc()'''

    @commands.command(aliases = ['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount:int = 5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member=None, *, reason = None):
        if member == ctx.author:
            await ctx.send("Oi you can't ban yourself.")
            return
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
    @commands.has_permissions(kick_members=True)
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
    @commands.has_permissions(manage_messages=True)
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
    @commands.has_permissions(manage_messages=True)
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

    @commands.group()
    @commands.guild_only()
    @commands.max_concurrency(1, per=commands.BucketType.guild)
    @commands.has_permissions(manage_messages=True)
    async def prune(self, ctx):
        """ Removes messages from the current server. """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    async def do_removal(self, ctx, limit, predicate, *, before=None, after=None, message=True):
        if limit > 2000:
            return await ctx.send(f'Too many messages to search given ({limit}/2000)')

        if before is None:
            before = ctx.message
        else:
            before = discord.Object(id=before)

        if after is not None:
            after = discord.Object(id=after)

        try:
            deleted = await ctx.channel.purge(limit=limit, before=before, after=after, check=predicate)
        except discord.Forbidden:
            return await ctx.send('I do not have permissions to delete messages.')
        except discord.HTTPException as e:
            return await ctx.send(f'Error: {e} (try a smaller search?)')

        deleted = len(deleted)
        if message is True:
            await ctx.send(f'🚮 Successfully removed {deleted} message{"" if deleted == 1 else "s"}.')

    @prune.command()
    async def embeds(self, ctx, search=100):
        """Removes messages that have embeds in them."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds))

    @prune.command()
    async def files(self, ctx, search=100):
        """Removes messages that have attachments in them."""
        await self.do_removal(ctx, search, lambda e: len(e.attachments))

    @prune.command()
    async def mentions(self, ctx, search=100):
        """Removes messages that have mentions in them."""
        await self.do_removal(ctx, search, lambda e: len(e.mentions) or len(e.role_mentions))

    @prune.command()
    async def images(self, ctx, search=100):
        """Removes messages that have embeds or attachments."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds) or len(e.attachments))

    @prune.command(name='all')
    async def _remove_all(self, ctx, search=100):
        
        await self.do_removal(ctx, search, lambda e: True)

    @prune.command()
    async def user(self, ctx, member: discord.Member, search=100):
        
        await self.do_removal(ctx, search, lambda e: e.author == member)

    @prune.command()
    async def contains(self, ctx, *, substr: str):
       
        if len(substr) < 3:
            await ctx.send('The substring length must be at least 3 characters.')
        else:
            await self.do_removal(ctx, 100, lambda e: substr in e.content)

    @prune.command(name='bots')
    async def _bots(self, ctx, search=100, prefix=None):
        """Removes a bot user's messages and messages with their optional prefix."""

        getprefix = prefix if prefix else self.config.prefix

        def predicate(m):
            return (m.webhook_id is None and m.author.bot) or m.content.startswith(tuple(getprefix))

        await self.do_removal(ctx, search, predicate)

    @prune.command(name='users')
    async def _users(self, ctx, prefix=None, search=100):
        """Removes only user messages. """

        def predicate(m):
            return m.author.bot is False

        await self.do_removal(ctx, search, predicate)

    @prune.command(name='emojis')
    async def _emojis(self, ctx, search=100):
        """Removes all messages containing custom emoji."""
        custom_emoji = re.compile(r'<a?:(.*?):(\d{17,21})>|[\u263a-\U0001f645]')

        def predicate(m):
            return custom_emoji.search(m.content)

        await self.do_removal(ctx, search, predicate)

    @prune.command(name='reactions')
    async def _reactions(self, ctx, search=100):
        """Removes all reactions from messages that have them."""

        if search > 2000:
            return await ctx.send(f'Too many messages to search for ({search}/2000)')

        total_reactions = 0
        async for message in ctx.history(limit=search, before=ctx.message):
            if len(message.reactions):
                total_reactions += sum(r.count for r in message.reactions)
                await message.clear_reactions()

        await ctx.send(f'Successfully removed {total_reactions} reactions.')

def setup(bot):
    bot.add_cog(Mod(bot))
