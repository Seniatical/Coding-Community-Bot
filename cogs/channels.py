import discord
import asyncio
from discord.ext import commands

class Help(commands.Cog, name = 'help'):

    def __init__ (self,bot):
        self.bot = bot
        self.bot.hp1 = False
        self.bot.hp2 = False

    @commands.Cog.listener()
    async def on_message(self,message):
        cata = self.bot.get_channel(756195945854795927)
        if message.author.guild_permissions.manage_messages == True:
            pass
        elif message.channel.id == 754710893538836480 and message.author.id != 755479510387916871:
            if self.bot.hp1 == True:
                pass
            else:
                embed = discord.Embed(title = f'You have just claimed {message.channel.name}.',
                 description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                embed.add_field(name = f'If you need someones attention: ', value = "Ping <@!726650418444107869>, they would be happy to help.")
                await message.channel.send(embed = embed)
                cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                await message.author.add_roles(cool)
                await message.channel.edit(category = cata, sync_permissions = True)
                self.bot.hp1 = True
                await asyncio.sleep(900)
                await message.author.remove_roles(cool)
        elif message.channel.id == 754710998769991680 and message.author.id != 755479510387916871:
            if self.bot.hp2 == True:
                pass
            else:
                embed = discord.Embed(title = f'You have just claimed {message.channel.name}.',
                 description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                embed.add_field(name = f'If you need someones attention: ', value = "Ping <@!726650418444107869>, they would be happy to help.")
                await message.channel.send(embed = embed)
                cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                await message.author.add_roles(cool)
                await message.channel.edit(category = cata, sync_permissions = True)
                self.bot.hp2 = True
                await asyncio.sleep(900)
                await message.author.remove_roles(cool)
        elif message.channel.id == 754711103665078273 and message.author.id != 7755479510387916871:
            if self.bot.hp2 == True:
                pass
            else:
                embed = discord.Embed(title = f'You have just claimed {message.channel.name}.',
                 description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                embed.add_field(name = f'If you need someones attention: ', value = "Ping <@!726650418444107869>, they would be happy to help.")
                await message.channel.send(embed = embed)
                cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                await message.author.add_roles(cool)
                await message.channel.edit(category = cata, sync_permissions = True)
                self.bot.hp2 = True
                await asyncio.sleep(900)
                await message.author.remove_roles(cool)

    @commands.command()
    async def close(self,ctx):
        cata = self.bot.get_channel(754710748353265745)
        if ctx.channel.id == 755862518567665776 or ctx.channel.id ==  755862540025725049 or ctx.channel.id == 756230480692641852 and ctx.author.id != 748331070927142985:
            await ctx.channel.edit(category = cata, sync_permissions = True)
            embed = discord.Embed(title = f"This channel is now open for help.",
             description = 'If you still need help, wait 15 minutes and then take another open channel.', color = discord.Colour.from_rgb(255,221,170))
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))
