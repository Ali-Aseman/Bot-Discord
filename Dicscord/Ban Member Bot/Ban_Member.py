import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix= '$')

@client.event
async def on_ready():
    print("Bot Is Run")

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

client.run('OTQ4NTE4Njc2NDM5NjUwMzE0.Yh8-2w.4x3tl22_B6xmeE629jAV-Dc0MZI')