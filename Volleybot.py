import discord
import os
from dotenv import load_dotenv as dot


Client = discord.client()
token = ''
mesage = "hi"
load_dotenv()


@client event
async def on_Ready():
    print(f'{client.user} has Connected to the discord Servers!)

def DMmembers():
    for member in guild.members:
        member.send(message)
        message.add_reaction(:Yes:)
        message.add_reaction(:No:)





client.run(token)
