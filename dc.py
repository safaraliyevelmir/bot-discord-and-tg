import discord
from discord.ext import commands
from djinni import djinni
from indeed import indeedbot

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)



@bot.event
async def on_ready():
    print("Ben hazırım")
    
    
@bot.event
async def on_message(message):
    # if message.content.split(" ")[0]=="job":
    #     for i in djinni.job_features("".join(message.content.split(" ")[1:])):        
    #         await message.channel.send(djinni.MAIN_URL+str(i))

    if message.content.split(" ")[0]=="job":
        for i in indeedbot.get_data(indeedbot.return_url("django")):
            #print(i)
            await message.channel.send(i)
    
bot.run("MTA4MDIzNzY5MjExNTIyNjY1NA.GSrqUs.3DKOZ_osUaavLMHLYT5nltkJR3sMQgGv7yMHRM")
