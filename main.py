# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=',', intents=intents)
#print(TOKEN)

#client = discord.Client(command_prefix=',', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_voice_state_update(member, before, after):
    username=member.name
    channelon = before.channel
    channeloff = after.channel
    if channelon and not channeloff:    
        print(f'member {username} left {channelon}')
    else:
        print(f'member {username} joined {channeloff}')
    #print(username, channelon, channeloff)

client.run(TOKEN)
