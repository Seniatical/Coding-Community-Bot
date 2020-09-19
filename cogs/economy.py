import json
import random
import discord
import traceback
from discord.ext import commands

mainshop = [{"name":"Watch","price":100,"description":"Time"},
            {"name":"Laptop","price":1000,"description":"Work"},
            {"name":"PC","price":10000,"description":"Gaming"}]

class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def helpeconomy(self,ctx):
        member = ctx.author
        embed = discord.Embed(title = 'Economy Commands', color = discord.Colour.green())
        embed.add_field(name = 'shop', value = 'Brings up the shop.')
        embed.add_field(name = 'buy', value = 'Buy an item from the shop.')
        embed.add_field(name = 'balance', value = 'Checks your balance.')
        embed.add_field(name = 'inv', value = 'Checks your inventory')
        embed.add_field(name = 'beg', value = 'Beg for money')
        embed.add_field(name = 'send', value = 'Send some money to another user.')
        embed.add_field(name = 'slots', value = 'Play slots')
        embed.add_field(name = 'rob', value = 'Rob a person of their money')
        embed.add_field(name = 'withdraw', value = 'Withdraw some money')
        embed.add_field(name = 'deposit', value = 'Deposit some money')
        embed.set_footer(icon_url = str(member.avatar_url), text = str(ctx.author))
        await ctx.send(embed = embed)

    @commands.command()
    async def shop(self,ctx):
        em = discord.Embed(title = "Shop")

        for item in mainshop:
            name = item["name"]
            price = item["price"]
            desc = item["description"]
            em.add_field(name = name, value = f"${price} | {desc}")

        await ctx.send(embed = em)



    @commands.command()
    async def buy(self,ctx,item,amount = 1):
        await self.open_account(ctx.author)

        res = await self.buy_this(ctx.author,item,amount)

        if not res[0]:
            if res[1]==1:
                await ctx.send("That Object isn't there!")
                return
            if res[1]==2:
                await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
                return


        await ctx.send(f"You just bought {amount} {item}")


    @commands.command()
    async def inv(self,ctx):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []


        em = discord.Embed(title = "Bag")
        for item in bag:
            name = item["item"]
            amount = item["amount"]

            em.add_field(name = name, value = amount)    

        await ctx.send(embed = em)  

    async def buy_this(self,user,item_name,amount):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                price = item["price"]
                break

        if name_ == None:
            return [False,1]

        cost = price*amount

        users = await self.get_bank_data()

        bal = await self.update_bank(user)

        if bal[0]<cost:
            return [False,2]


        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt + amount
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                    break
                index+=1 
            if t == None:
                obj = {"item":item_name , "amount" : amount}
                users[str(user.id)]["bag"].append(obj)
        except:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"] = [obj]        

        with open("mainbank.json","w") as f:
            json.dump(users,f)

        await self.update_bank(user,cost*-1,"wallet")

        return [True,"Worked"]

    @commands.command()
    async def bag(self,ctx):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []


        em = discord.Embed(title = "Bag")
        for item in bag:
            name = item["item"]
            amount = item["amount"]

            em.add_field(name = name, value = amount)    

        await ctx.send(embed = em) 



    @commands.command()
    async def balance(self,ctx):
        try:
            await self.open_account(ctx.author)
            users = await self.get_bank_data()
            user = ctx.author
            wallet_amt = users[str(user.id)]["wallet"]
            bank_amt = users[str(user.id)]['bank']
            embed = discord.Embed(title = f"{ctx.author}'s balance", color = discord.Colour(0xff69b4))
            embed.add_field(name = "Wallet balance", value = wallet_amt)
            embed.add_field(name = "Bank balance", value = bank_amt)
            await ctx.send(embed = embed)
        except Exception:
            traceback.print_exc()

    async def open_account(self,user):
        try:
            users = await self.get_bank_data()
            if str(user.id) in users:
                return False
            else:
                users[str(user.id)]={}
                users[str(user.id)]["wallet"] = 0
                users[str(user.id)]["bank"] = 0

            with open("mainbank.json", "w") as f:
                json.dump(users, f)
            return True
        except Exception:
            traceback.print_exc()

    async def get_bank_data(self):
        with open("mainbank.json", "r+") as f:
            users = json.load(f)
        return users

    async def update_bank(self,user,change = 0,mode = "wallet"):
        users = await self.get_bank_data()

        users[str(user.id)][mode] += change

        with open("mainbank.json","w") as f:
            json.dump(users, f)

        bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
        return bal

    @commands.command()
    async def withdraw(self,ctx,amount = None):
        await self.open_account(ctx.author)
        if amount == None:
            await ctx.send("Please enter the amount to withdraw")
            return
        
        bal = await self.update_bank(ctx.author)
        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send('Amount must be positive!')
            return
        await self.update_bank(ctx.author,amount)
        await self.update_bank(ctx.author,-1*amount,"bank")
        await ctx.send(f"You withdrew {amount} coins!")

    @commands.command()
    async def deposit(self,ctx,amount = None):
        await self.open_account(ctx.author)
        if amount == None:
            await ctx.send("Please enter the amount to withdraw")
            return

        bal = await self.update_bank(ctx.author)
        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send('Amount must be positive!')
            return
        await self.update_bank(ctx.author,-1*amount)
        await self.update_bank(ctx.author,amount,"bank") 
        await ctx.send(f"You deposited {amount} coins!")
        
    @commands.command()
    async def send(self,ctx,member: discord.Member, amount = None):
        await self.open_account(ctx.author)
        await self.open_account(member)
        
        if amount == None:
            await ctx.send("Please enter the amount to withdraw")
            return

        bal = await self.update_bank(ctx.author)
        amount = int(amount)
        if amount>bal[0]:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send('Amount must be positive!')
            return
        await self.update_bank(ctx.author,-1*amount, "bank")
        await self.update_bank(member,amount,"bank")
        await ctx.send(f"You gave {amount} coins!")

    @commands.command()
    async def slots(self,ctx,amount = None):
        await self.open_account(ctx.author)
        if amount == None:
            await ctx.send("Please enter the amount to withdraw.")
            return

        bal = await self.update_bank(ctx.author)
        amount = int(amount)
        if amount>bal[0]:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send('Amount must be positive!')
            return
        
        final = []
        for i in range(3):
            a = random.choice(["X","O","Q"])

            final.append(a)

        await ctx.send(str(final))     

        if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
            await self.update_bank(ctx.author,2*amount)
            await ctx.send("You Won!")
        else:
            await self.update_bank(ctx.author,-1*amount)
            await ctx.send("You Lost.")

    @commands.command()
        await self.open_account(ctx.author)
        await self.open_account(member)

        bal = await self.update_bank(member)
        if bal[0]<100:
            await ctx.send("It's not worth it!")
            return

        earnings = random.randrange(0,bal[0])

        
        await self.update_bank(ctx.author,earnings)
        await self.update_bank(member,-1*earnings)
        await ctx.send(f"You robbed and got {earnings} coins!")
    
    @commands.command()
    async def beg(self,ctx):
        await self.open_account(ctx.author)
        users = await self.get_bank_data()
        user = ctx.author
        earnings = random.randrange(101)


        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json","w") as f:
            json.dump(users,f)
#work cmd in main file

def setup(bot):
    bot.add_cog(Economy(bot))
