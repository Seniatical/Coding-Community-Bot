import discord
import datetime
import traceback
from discord.ext import commands

class Modmail(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        gd = self.bot.get_guild(759198536662646835)
        mem = gd.get_role(759199029186920448)
        chk = gd.get_member(message.author.id)
        chk = chk.roles
        for x in chk:
            if not mem in chk and message.guild == None:
                return
        if message.guild == None:
            embed = discord.Embed(title = "Message Sent!", color = discord.Colour.green())
            embed.add_field(name = "Message ID: ", value = message.id, inline = False)
            embed.add_field(name = "Message Sent at: ", value = datetime.datetime.utcnow().strftime('%a, %d %B %Y, %I:%M %p UTC'), inline = False)
            embed.add_field(name = "Message: ", value = message.content, inline = False)
            await message.author.send(embed = embed)
            channel = self.bot.get_channel(764237890162524180)
            mod = discord.Embed(title = f"{message.author}'s Message:", color = discord.Colour.dark_gold())
            mod.add_field(name = "Members id: ", value = message.author.id)
            mod.add_field(name = "Message Sent at: ", value = datetime.datetime.utcnow().strftime('%a, %d %B %Y, %I:%M %p UTC'), inline = False)
            mod.add_field(name = "Message ID: ", value = message.id, inline = False)
            mod.add_field(name = "Message: ", value = message.content)
            await channel.send(embed = mod)

    @commands.command()
    @commands.has_any_role("Owner","Head Moderator","Moderator","Trainee Moderator")
    async def reply(self,ctx,msg_id,*,response):
        try:
            await ctx.message.delete()
            channel = self.bot.get_channel(764237890162524180)
            reply_to = await channel.fetch_message(int(msg_id))
            member = ctx.guild.get_member(int(reply_to.embeds[0].fields[0].value))
            embed = discord.Embed(title = f"{ctx.author} Has replied to you", color = discord.Colour.blue())
            embed.add_field(name = "Message Replied at: ", value = datetime.datetime.utcnow().strftime('%a, %d %B %Y, %I:%M %p UTC'), inline = False)
            embed.add_field(name = "Moderator's Name: ", value = ctx.author)
            embed.add_field(name = "Moderator's ID: ", value = ctx.author.id)
            embed.add_field(name = "Reply: ", value = response, inline = False)
            await member.send(embed = embed)
            chan2 = self.bot.get_channel(9764257169846960188)
            await chan2.send(embed = embed)
        except Exception as e:
            traceback.print_exc()

    @commands.command()
    @commands.has_any_role("Owner","Head Moderator","Moderator","Trainee Moderator")
    async def end(self,ctx,msg_id,*,reason = "No reason Provided"):
        channel = self.bot.get_channel(764237890162524180)
        reply_to = await channel.fetch_message(int(msg_id))
        member = ctx.guild.get_member(int(reply_to.embeds[0].fields[0].value))
        embed = discord.Embed(title = f"{ctx.author} has closed the session.", color = discord.Colour.red())
        embed.add_field(name = 'Reason for Closure: ', value = str(reason))
        embed.add_field(name = "Message Closed at: ", value = datetime.datetime.utcnow().strftime('%a, %d %B %Y, %I:%M %p UTC'), inline = False)
        embed.add_field(name = "Moderator's Name: ", value = ctx.author)
        embed.add_field(name = "Moderator's ID: ", value = ctx.author.id)
        await member.send(embed = embed)
 
def setup(bot):
    bot.add_cog(Modmail(bot))
