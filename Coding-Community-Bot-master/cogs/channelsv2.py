import discord
import io
import sys
import asyncio
import contextlib
import traceback
import datetime
from discord.ext import commands, tasks

class Channels(commands.Cog, name = 'channels'):

    def __init__ (self,bot):
        self.bot = bot
        self.bot.hp1 = False
        self.bot.hp2 = False
        self.bot.hp3 = False
        self.bot.hp4 = False
        self.bot.hp5 = False
        self.active1 = False
        self.active2 = False
        self.active3 = False
        self.active4 = False
        self.active5 = False
        self.user1 = None
        self.user2 = None
        self.user3 = None
        self.user4 = None
        self.user5 = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.act_check.start()

    @tasks.loop(seconds = 5)
    async def act_check(self):
        await self.check_activity()

    async def check_activity(self):
        channels = ['754710893538836480','754710998769991680','754711103665078273','762722834861523045','762866574133952593']
        rn = datetime.datetime.utcnow()
        for x in channels:
            channel = self.bot.get_channel(int(x))
            try:
                chk = await channel.history(limit = 1).next()
                idle = rn - chk.created_at
                idle = idle.total_seconds()
            
                if int(x) == 754710893538836480 and idle > 600 and self.bot.hp1 == True:
                    self.active1 = False
                elif int(x) == 754710998769991680 and idle > 600 and self.bot.hp2 == True:
                    self.active2 = False
                elif int(x) == 754711103665078273 and idle > 600 and self.bot.hp3 == True:
                    self.active3 = False
                elif int(x) == 762722834861523045 and idle > 600 and self.bot.hp4 == True:
                    self.active4 = False
                elif int(x) == 762866574133952593 and idle > 600 and self.bot.hp5 == True:
                    self.active5 = False
                if int(x) == 754710893538836480 and idle < 600 and self.bot.hp1 == True:
                    self.active1 = True
                elif int(x) == 754710998769991680 and idle < 600 and self.bot.hp2 == True:
                    self.active2 = True
                elif int(x) == 754711103665078273 and idle < 600 and self.bot.hp3 == True:
                    self.active3 = True
                elif int(x) == 762722834861523045 and idle < 600 and self.bot.hp4 == True:
                    self.active4 = True
                elif int(x) == 762866574133952593 and idle < 600 and self.bot.hp5 == True:
                    self.active5 = True
            except:
                pass

    @commands.Cog.listener()
    async def on_message(self,message):
        try:
            help_channels = [754710893538836480,754710893538836480,754711103665078273,762722834861523045,762866574133952593]
            try:
                role = discord.utils.get(message.guild.roles, name = 'On Patrol Helper 🚨')
            except:
                pass
            if message.author.guild_permissions.manage_messages == True:
                return
            elif message.channel.id == 754710893538836480 and message.author.bot == False:
                #763187874911879169
                if self.bot.hp1 == True:
                    pass
                else:
                    if self.bot.hp1 == False:
                        embed = discord.Embed(title = f'You have just claimed ❌ help-α.',
                        description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                        embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                        embed.add_field(name = f'If you need someones attention: ', value = f"Ping {role.mention}, they would be happy to help.")
                        await message.channel.send(embed = embed)
                        cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                        await message.channel.set_permissions(cool, send_messages = True)
                        await message.author.add_roles(cool)
                        self.bot.hp1 = True
                        self.active1 = True
                        try:
                            await message.channel.edit(name = f"❌help-α (Occupied)")
                        except Exception:
                            traceback.print_exc()
                        await asyncio.sleep(900)
                        while True:
                            while self.active1 == True:
                                await asyncio.sleep(300)
                                await message.author.remove_roles(cool)
                            if self.active1 == False and self.bot.hp1 == True:
                                await message.channel.edit(name = f"🔐help-α (Cooldown)")
                                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                                msg = await message.channel.send(embed = embed2)
                                mem = discord.utils.get(message.guild.roles, name = "Member")
                                await message.channel.set_permissions(mem, send_messages = False)
                                await asyncio.sleep(600)
                                await message.channel.set_permissions(mem, send_messages = None)
                                await message.channel.edit(name = f"✅help-α (Available)")
                                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                                 description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                                await msg.edit(embed = embed3)
                                self.bot.hp1 = False
                                break
            elif message.channel.id == 754710998769991680 and message.author.bot == False:
                #763187874911879169
                if self.bot.hp2 == True:
                    pass
                else:
                    if self.bot.hp2 == False:
                        embed = discord.Embed(title = f'You have just claimed ❌ help-β.',
                        description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                        embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                        embed.add_field(name = f'If you need someones attention: ', value = f"Ping {role.mention}, they would be happy to help.")
                        await message.channel.send(embed = embed)
                        cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                        await message.channel.set_permissions(cool, send_messages = True)
                        await message.author.add_roles(cool)
                        self.bot.hp2 = True
                        self.active2 = True
                        try:
                            await message.channel.edit(name = f"❌help-β (Occupied)")
                        except Exception:
                            traceback.print_exc()
                        await asyncio.sleep(900)
                        while True:
                            while self.active2 == True:
                                await asyncio.sleep(300)
                                await message.author.remove_roles(cool)
                            if self.active2 == False and self.bot.hp2 == True:
                                await message.channel.edit(name = f"🔐help-β (Cooldown)")
                                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                                msg = await message.channel.send(embed = embed2)
                                mem = discord.utils.get(message.guild.roles, name = "Member")
                                await message.channel.set_permissions(mem, send_messages = False)
                                await asyncio.sleep(600)
                                await message.channel.set_permissions(mem, send_messages = None)
                                await message.channel.edit(name = f"✅help-β (Available)")
                                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                                 description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                                await msg.edit(embed = embed3)
                                self.bot.hp2 = False
                                break
            elif message.channel.id == 754711103665078273 and message.author.bot == False:
                #763187874911879169
                if self.bot.hp3 == True:
                    pass
                else:
                    if self.bot.hp3 == False:
                        embed = discord.Embed(title = f'You have just claimed ❌ help-γ.',
                        description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                        embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                        embed.add_field(name = f'If you need someones attention: ', value = f"Ping {role.mention}, they would be happy to help.")
                        await message.channel.send(embed = embed)
                        cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                        await message.channel.set_permissions(cool, send_messages = True)
                        await message.author.add_roles(cool)
                        self.bot.hp3 = True
                        self.active3 = True
                        try:
                            await message.channel.edit(name = f"❌help-γ (Occupied)")
                        except Exception:
                            traceback.print_exc()
                        await asyncio.sleep(900)
                        while True:
                            while self.active3 == True:
                                await asyncio.sleep(300)
                                await message.author.remove_roles(cool)
                            if self.active3 == False and self.bot.hp3:
                                await message.channel.edit(name = f"🔐help-γ (Cooldown)")
                                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                                msg = await message.channel.send(embed = embed2)
                                mem = discord.utils.get(message.guild.roles, name = "Member")
                                await message.channel.set_permissions(mem, send_messages = False)
                                await asyncio.sleep(600)
                                await message.channel.set_permissions(mem, send_messages = None)
                                await message.channel.edit(name = f"✅help-γ (Available)")
                                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                                 description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                                await msg.edit(embed = embed3)
                                self.bot.hp3 = False
                                break
            elif message.channel.id == 762722834861523045 and message.author.bot == False:
                #763187874911879169
                if self.bot.hp4 == True:
                    pass
                else:
                    if self.bot.hp4 == False:
                        embed = discord.Embed(title = f'You have just claimed ❌ help-δ.',
                        description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                        embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                        embed.add_field(name = f'If you need someones attention: ', value = f"Ping {role.mention}, they would be happy to help.")
                        await message.channel.send(embed = embed)
                        cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                        await message.channel.set_permissions(cool, send_messages = True)
                        await message.author.add_roles(cool)
                        self.bot.hp4 = True
                        self.active4 = True
                        try:
                            await message.channel.edit(name = f"❌help-δ (Occupied)")
                        except Exception:
                            traceback.print_exc()
                        await asyncio.sleep(900)
                        while True:
                            while self.active4 == True:
                                await asyncio.sleep(300)
                                await message.author.remove_roles(cool)
                            if self.active4 == False and self.bot.hp4:
                                await message.channel.edit(name = f"🔐help-δ (Cooldown)")
                                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                                msg = await message.channel.send(embed = embed2)
                                mem = discord.utils.get(message.guild.roles, name = "Member")
                                await message.channel.set_permissions(mem, send_messages = False)
                                await asyncio.sleep(600)
                                await message.channel.set_permissions(mem, send_messages = None)
                                await message.channel.edit(name = f"✅help-δ (Available)")
                                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                                 description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                                await msg.edit(embed = embed3)
                                self.bot.hp4 = False
                                break
            elif message.channel.id == 762866574133952593 and message.author.bot == False:
                #763187874911879169
                if self.bot.hp5 == True:
                    pass
                else:
                    if self.bot.hp5 == False:
                        embed = discord.Embed(title = f'You have just claimed ❌ help-ε.',
                        description = 'You would not be able to claim any other help channels for 15 minutes.', color = discord.Colour.from_rgb(255,221,170))
                        embed.add_field(name = f'When asking questions: ', value = "Don't just say `i need help`, just state your question and hopefully someone comes to help.")
                        embed.add_field(name = f'If you need someones attention: ', value = f"Ping {role.mention}, they would be happy to help.")
                        await message.channel.send(embed = embed)
                        cool = discord.utils.get(message.guild.roles, name = 'Cooldown')
                        await message.channel.set_permissions(cool, send_messages = True)
                        await message.author.add_roles(cool)
                        self.bot.hp5 = True
                        self.active5 = True
                        try:
                            await message.channel.edit(name = f"❌help-ε (Occupied)")
                        except Exception:
                            traceback.print_exc()
                        await asyncio.sleep(900)
                        while True:
                            while self.active5 == True:
                                await asyncio.sleep(300)
                                await message.author.remove_roles(cool)
                            if self.active5 == False and self.bot.hp5:
                                await message.channel.edit(name = f"🔐help-ε (Cooldown)")
                                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                                msg = await message.channel.send(embed = embed2)
                                mem = discord.utils.get(message.guild.roles, name = "Member")
                                await message.channel.set_permissions(mem, send_messages = False)
                                await asyncio.sleep(600)
                                await message.channel.set_permissions(mem, send_messages = None)
                                await message.channel.edit(name = f"✅help-ε (Available)")
                                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                                 description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                                await msg.edit(embed = embed3)
                                self.bot.hp5 = False
                                break
            
        except Exception:
            traceback.print_exc()
                    
    @commands.command()
    async def close(self,ctx):
        if ctx.channel.id == 754710893538836480 or ctx.channel.id == 754710998769991680 or ctx.channel.id == 754711103665078273 or ctx.channel.id == 762722834861523045 or ctx.channel.id == 762866574133952593 and ctx.author.id != 7755479510387916871:
            embed = discord.Embed(title = f"This channel is now on cooldown",
             description = 'If you still need help, wait 15 minutes and then take another open channel.', color = discord.Colour.from_rgb(255,221,170))
            msg = await ctx.send(embed = embed)
            if ctx.channel.id == 754710893538836480:
                await ctx.channel.edit(name = f"🔐help-α (Cooldown)")
                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                msg = await ctx.channel.send(embed = embed2)
                self.bot.hp1 = False
                mem = discord.utils.get(ctx.guild.roles, name = "Member")
                await ctx.channel.set_permissions(mem, send_messages = False)
                await asyncio.sleep(600)
                await ctx.channel.edit(name = f"✅help-α (Available)")
                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                await msg.edit(embed = embed3)
            elif ctx.channel.id == 754710998769991680:
                await ctx.channel.edit(name = f"🔐help-β (Cooldown)")
                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                msg = await ctx.channel.send(embed = embed2)
                self.bot.hp2 = False
                mem = discord.utils.get(ctx.guild.roles, name = "Member")
                await ctx.channel.set_permissions(mem, send_messages = False)
                await asyncio.sleep(600)
                await ctx.channel.edit(name = f"✅help-β (Available)")
                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                await msg.edit(embed = embed3)
            elif ctx.channel.id == 754711103665078273:
                await ctx.channel.edit(name = f"🔐help-γ (Cooldown)")
                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                msg = await ctx.channel.send(embed = embed2)
                self.bot.hp3 = False
                mem = discord.utils.get(ctx.guild.roles, name = "Member")
                await ctx.channel.set_permissions(mem, send_messages = False)
                await asyncio.sleep(600)
                await ctx.channel.edit(name = f"✅help-γ (Available)")
                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                await msg.edit(embed = embed3)
            elif ctx.channel.id == 762722834861523045:
                await ctx.channel.edit(name = f"🔐help-δ (Cooldown)")
                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                msg = await ctx.channel.send(embed = embed2)
                self.bot.hp4 = False
                mem = discord.utils.get(ctx.guild.roles, name = "Member")
                await ctx.channel.set_permissions(mem, send_messages = False)
                await asyncio.sleep(600)
                await ctx.channel.edit(name = f"✅help-δ (Available)")
                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                await msg.edit(embed = embed3)
            elif ctx.channel.id == 762866574133952593:
                await ctx.channel.edit(name = f"🔐help-ε (Cooldown)")
                embed2 = discord.Embed(title = 'This channel was closed due to inactivity.',
                description = 'This channel is now on cooldown, if you still need help, claim another channel.', color = discord.Colour.from_rgb(255,221,170))
                msg = await ctx.channel.send(embed = embed2)
                self.bot.hp5 = False
                mem = discord.utils.get(ctx.guild.roles, name = "Member")
                await ctx.channel.set_permissions(mem, send_messages = False)
                await asyncio.sleep(600)
                await ctx.channel.edit(name = f"✅help-ε (Available)")
                embed3 = discord.Embed(title = "This Channel is Now Available! ✅",
                description = "Anyone can now claim this channel.", color = discord.Colour.from_rgb(255,221,170))
                await msg.edit(embed = embed3)
            

    @commands.command(aliases = ['verifythem'])
    async def vt(self,ctx, member:discord.Member):
        role = discord.utils.get(ctx.guild.roles, name = 'Member')
        await member.add_roles(role)
        take = discord.utils.get(ctx.guild.roles, name = 'Unverified')
        await member.remove_roles(take)
        await ctx.send(f"{member.mention} Has been Successfully Verified!")
                
    '''@commands.command()
    async def eval(self,ctx,*,code:str):
        try:
            if code.startswith('```py') and code.endswith('```'):
                code = code[5:-3]
            elif code.startswith('`') and code.endswith('`'):
                code = code[1:-1]
            @contextlib.contextmanager
            def evaluate(stdout = None):
                old = sys.stdout
                if stdout == None:
                    sys.stdout = io.StringIO()
                yield sys.stdout
                sys.stdout = old
            
            with evaluate() as e:
                exec(code, {})

            msg = await ctx.send('Evaluating...')
            await msg.delete()
            await ctx.send(f"{ctx.author.mention} Finished Evaluating!")
            embed = discord.Embed(title = f'Results: \n', description = e.getvalue(), color = discord.Colour.from_rgb(255,221,170))
            await ctx.send(embed = embed)
        except Exception as e:
            embed = discord.Embed(title = 'Ran into a error while evaluating...')
            embed.add_field(name = 'Error: ', value = e)
            await ctx.send(embed = embed)'''

def setup(bot):
    bot.add_cog(Channels(bot))
