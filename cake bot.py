#cake bot code
import discord, logging, sqlite3
from discord.ext import commands
from random import randint

bot = discord.Client(command_prefix='', description='Hi.')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    #await bot.send_message(bot.get_channel("338581958395297802"), "Waawaaweewaa we are logged on!") #comment this out if ur testing

#on a message
@bot.event
async def on_message(message):
    if message.author.id == "97742542602264576":
        await bot.send_message(message.channel, "hey, it cake")
    elif ("cake" in message.content or "hey" in message.content) and message.author.id != "414179265064468480":
        await bot.send_message(message.channel, "hey, it's me cake")


#runs bot
bot.run('NDE0MTc5MjY1MDY0NDY4NDgw.DWjmYg.pj4WcRCj752qp-g8VS4WUx17Sb4')


#https://discordapp.com/api/oauth2/authorize?client_id=414179265064468480&scope=bot&permissions=0
