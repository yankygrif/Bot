import discord
from discord.ext import commands
import datetime
import random

playerlist=[]
bot = commands.Bot(command_prefix='>', description="This is a RollerBot")

@bot.command()
async def roll(ctx, string, bonus=0):
    if "d" in string:
        inf=string.split("d")
    elif "D" in string:
        inf=string.split("D")
    if int(bonus)<=0 or int(bonus)>=0:
        bonus=int(bonus)
    else:
        bonus=0
    amount=int(inf[0])
    number=int(inf[1])
    suma=0
    for i in range(amount):
        a=random.randint(1,number)
        message="Rolled for "+str(a+bonus)
        await ctx.send(message)
        suma=suma+a
    if amount>=2:
        total="Total sum is equal to="+str(suma)
        await ctx.send(total)

@bot.command()
async def damage(ctx, dicetype, disetype2, damage, bonus=0, bonus2=0, crit=False):

    if "d" in dicetype:
        inf=dicetype.split("d")
    elif "D" in dicetype:
        inf=dicetype.split("D")

    if "d" in disetype2:
        inf2=disetype2.split("d")
    elif "D" in disetype2:
        inf2=disetype2.split("D")

    if "d" in damage:
        damage=damage.split("d")
    elif "D" in damage:
        damage=damage.split("D")

    if int(bonus)<=0 or int(bonus)>=0:
        bonus=int(bonus)
    else:
        bonus=0

    if int(bonus2)<=0 or int(bonus2)>=0:
        bonus2=int(bonus2)
    else:
        bonus2=0
    res1=random.randint(1,int(inf[1]))+bonus
    res2=random.randint(1,int(inf2[1]))+bonus2
    message="\n1-st Rolled for:"+str(res1)+"\n2-nd Rolled for:"+str(res2)
    
    if res1>=res2:
        dmgroll=random.randint(1,int(damage[1]))
        if crit==True and dmgroll>=int(damage[1]):
            dmgroll=dmgroll+random.randint(1,int(damage[1]))
            msg=message+"\nCrit damage="+str(dmgroll)
            await ctx.send(msg)
        else:
            msg=message+"\nDamage="+str(dmgroll)
            await ctx.send(msg)
    else:
        msg=message+"\nNo damage looser"
        await ctx.send(msg)

@bot.command()
async def registrate(ctx, name, role):
    file=open("playerlist.txt",'a')
    text=str("\n "+str(ctx.message.author)+" said:\n would be "+ str(name) + "\nwith role:"+str(role))
    file.write(text)
    file.close()
            
@bot.command()
async def source(ctx):
    await ctx.send("https://github.com/yankygrif/RollerBot/blob/main/copy%20OfBot.py")

@bot.command()
async def getplayers(ctx):
    for i in playerlist:
        player=i
        await ctx.send("{}".format(player.mention))
       
@bot.command()
async def addplayer(ctx):
    if ctx.message.author in playerlist:
        pass
    else:
        playerlist.append(ctx.message.author)
    
    

@bot.command(pass_context=True)
async def name(ctx):
    await ctx.send("{} is your name".format(ctx.message.author.mention))
   

    
# Events
@bot.event
async def on_ready():
    print("sus")


@bot.listen()
async def on_message(message):
    pass

bot.run("token")
