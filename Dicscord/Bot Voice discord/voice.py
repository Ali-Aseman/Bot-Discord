from discord.ext import commands
import discord
from asyncio import *


class config:
    token = 'OTQ4NDYwNjYwNjg4MzA2MTc2.Yh8I0w.bks0tPeHbYVN6bDLy8-XaZPkzYo'
    prefix = '$'

client = commands.Bot(command_prefix=config.prefix)
voice_object = None

@client.event
async def on_ready():
    print("Bot Voice_Hell Is Run ")

@client.command()
async def join(ctx):
    global voice_object
    my_channel = ctx.message.author.voice.channel
    voice_object = await my_channel.connect()
    await ctx.send('Joined The Voice !')


@client.command()
async def disconnect(ctx):
    global voice_object
    if voice_object != None:
        await my_channel.disconnect()
        voice_object = None
        await ctx.send('Disconnected !')
    else:
        await ctx.send('Disconnected In Voice')
client.run(config.token)
