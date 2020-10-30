import discord
import asyncio
import random
import traceback
import datetime
from discord.ext import commands

class Ticket(commands.Cog, name = 'ticket'):

    def __init__(self,bot):
        self.bot = bot
        self.tc1 = False
        self.tc2 = False
        self.active = []
        self.inactive = [764302823395033099,764302978617704468]

    @commands.command(aliases = ['newticket','ticket','open'])
    async def new(self,ctx):
        try:
            if ctx.channel.id == 764293795247947847:
                guild = ctx.message.guild
                embed = discord.Embed(title = 'A new Channel has been opened for you!', color = discord.Colour.teal())
                cate = self.bot.get_channel(759454850370502737)
                choc = random.choice(self.inactive)
                channel = self.bot.get_channel(choc)
                self.active.append(choc)
                self.inactive.remove(choc)
                await channel.edit(category = cate, sync_permissions = True)
                await channel.set_permissions(ctx.author, read_messages = True)
                cooldown = discord.utils.get(ctx.guild.roles, name = 'Ticket Cooldown')
                embed = discord.Embed(title = 'You have successfully opened a support ticket! :white_check_mark:', color = discord.Colour.green())
                await ctx.send(embed = embed)
                await channel.send(ctx.author.mention + ' Your ticket has just been opened.')
                embed = discord.Embed(title = f'{ctx.author}, You have just created a ticket, a staff member will come here soon.',
                description = 'Meanwhile, please state your question in a clear and descriptive way.', color = discord.Colour.teal())
                embed.add_field(name = "This channel is for support such as needing to contact a mod privatly.", value = "This is not a help channel, please do not ask code related issues here.")
                embed.add_field(name = "Channel Opened at: ", value = datetime.datetime.utcnow().strftime('%a, %d %B %Y, %I:%M %p UTC') + " by " + str(ctx.author))
                await channel.send(embed = embed)
                await ctx.author.add_roles(cooldown)
                await asyncio.sleep(3200)
                await ctx.author.remove_roles(cooldown)
            else:
                pass
        except Exception:
            traceback.print_exc()

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def closeticket(self,ctx,*, reason = 'No reason provided.'):
        try:
            if ctx.channel.id == 764302823395033099:
                cate = self.bot.get_channel(764304798610227200)
                embed = discord.Embed(title = f'Channel closed by {ctx.author}',description = "This channel will Close in 10 seconds.", color = discord.Colour.red())
                embed.add_field(name = "Reason for closure: ", value = reason)
                await ctx.send(embed = embed)
                await asyncio.sleep(10)
                await ctx.channel.set_permissions(ctx.author, read_messages = False)
                await ctx.channel.edit(category = cate, sync_permissions = True)
                self.inactive.append(ctx.channel.id)
                self.active.remove(ctx.channel.id)
                self.tc1 = False
            elif ctx.channel.id == 764302978617704468:
                cate = self.bot.get_channel(764304798610227200)
                embed = discord.Embed(title = f'Channel closed by {ctx.author}',description = "This channel will Close in 10 seconds.", color = discord.Colour.red())
                embed.add_field(name = "Reason for closure: ", value = reason)
                await ctx.send(embed = embed)
                await asyncio.sleep(10)
                await ctx.channel.set_permissions(ctx.author, read_messages = False)
                await ctx.channel.edit(category = cate, sync_permissions = True)
                self.inactive.append(ctx.channel.id)
                self.active.remove(ctx.channel.id)
                self.tc2 = False
        except AttributeError:
            pass
        except Exception:
            traceback.print_exc()
        

def setup(bot):
    bot.add_cog(Ticket(bot))