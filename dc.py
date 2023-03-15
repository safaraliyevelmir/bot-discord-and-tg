from candidate import Candidate
import discord
from discord.ext import commands
from djinni import djinni
from indeed import indeedbot
from remoteco import remotebot
from jobot import jobot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)



@bot.event
async def on_ready():
    print("Ben hazırım")
    
    
@bot.event
async def on_message(message):

    if message.content.split(" ")[0]=="job":
        for i in djinni.job_features("+".join(message.content.split(" ")[1:]))[:5]:        
            await message.channel.send(djinni.MAIN_URL+str(i))

        for i in jobot.get_data(jobot.return_url("+".join(message.content.split(" ")[1:])))[:5]:
            await message.channel.send(i)

        for i in indeedbot.get_data(indeedbot.return_url("+".join(message.content.split(" ")[1:])))[:5]:
            await message.channel.send(i)

        for i in remotebot.get_data(remotebot.return_url("+".join(message.content.split(" ")[1:])))[:5]:
            await message.channel.send(i)
        


bot.run("MTA4MDIzNzY5MjExNTIyNjY1NA.GpK4W0._Mmm1D2Qkxu3K1-RXXg6mBxapeNBlqPB8XGHS4")
