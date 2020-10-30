import discord
from discord.ext import commands
import datetime
import asyncio
import traceback

class Suggestions(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases = ['sug', 'suggestion'])
    @commands.cooldown(1,21600, commands.BucketType.user)
    async def suggest(self,ctx,*,suggestion):
        await ctx.message.delete()
        #729711188392280154 production id
        channel = self.bot.get_channel(729711188392280154)
        embed = discord.Embed(title = f"Suggestion from: {ctx.author}", color = discord.Colour.blue())
        embed.set_author(name = f"{ctx.author}", icon_url = ctx.author.avatar_url)
        embed.add_field(name = "Author's Suggestion: ", value = str(suggestion))
        msg = await channel.send(embed = embed)
        await msg.add_reaction('\U00002705')
        await msg.add_reaction('❌')
        embed = discord.Embed(title = f"{ctx.author}, your suggestion has been successfully submitted! Check #💡suggestions")
        msg2 = await ctx.send(embed = embed)
        await asyncio.sleep(10)
        await msg2.delete()

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def approve(self,ctx,msg_id,*,reason = 'No reason provided by approver'):
        try:
            await ctx.message.delete()
            channel = self.bot.get_channel(729711188392280154)
            msg = await channel.fetch_message(int(msg_id))
            embed = discord.Embed(title = f"{msg.embeds[0].title}", color = discord.Colour.green())
            embed.set_author(name = f"{ctx.author}", icon_url = ctx.author.avatar_url)
            embed.add_field(name = "Approved Suggestion: ", value = str(msg.embeds[0].fields[0].value))
            embed.add_field(name = f"**Suggestion Approved by {ctx.author}**", value = f"Reason for Approval: {reason}", inline = False)
            await msg.edit(embed = embed)
        except Exception:
            traceback.print_exc()

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def deny(self,ctx,msg_id,*,reason = 'No reason provided by denier'):
        try:
            await ctx.message.delete()
            channel = self.bot.get_channel(729711188392280154)
            msg = await channel.fetch_message(int(msg_id))
            embed = discord.Embed(title = f"{msg.embeds[0].title}", color = discord.Colour.red())
            embed.set_author(name = f"{ctx.author}", icon_url = ctx.author.avatar_url)
            embed.add_field(name = "Denied Suggestion: ", value = str(msg.embeds[0].fields[0].value))
            embed.add_field(name = f"**Suggestion Denied by {ctx.author}**", value = f"Reason for Denial: {reason}", inline = False)
            await msg.edit(embed = embed)
        except Exception:
            traceback.print_exc()
    

def setup(bot):
    bot.add_cog(Suggestions(bot))