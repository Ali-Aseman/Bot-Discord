from dis import disco
import discord
from discord.ext import commands
from asyncio import *
import youtube_dl
import os

class config:
    token = 'OTQ4MTI0NTc0NzA3NTExMzI4.Yh3P0Q.BnO6KahvgzYZWFa30DYkfk43HrM'
    prefix = '$'

client = commands.Bot(command_prefix=config.prefix)
# client.remove_command('help')
@client.event
async def on_ready():
    print('Bot Code_Hell Is Run')

@client.command()
async def cmd(ctx):
    mention = ctx.author.mention
    avatar = ctx.author.avatar_url
    # userid = ctx.author.id
    await ctx.send('Hi' + "  " + str(mention))


# @client.command()
# async def setstatus(ctx, status_type):
#     if(status_type == "one"):
#         await ctx.send("status be meghdar One taghir kard")
#         await client.change_presence(status=discord.Status.one)

#     elif(status_type == "dnd"):
#         await ctx.send("status be meghdar Dnd taghir kard")
#         await client.change_presence(status=discord.Status.dnd)

#     else:
#         await ctx.send("status be meghdar Obn taghir kard")
#         await client.change_presence(status=discord.Status.obn)


@client.command()
async def clear(ctx, count='10'):
    count = int(count)
    await ctx.channel.purge(limit=count)
    await ctx.send(">>>"+ " " + str(count)+' Massage Deleted !')



@client.command(pass_context=True)
async def image_1(ctx):
    await ctx.send(file=discord.File('ghostemane.jpg'))

@client.command()
async def virus_1(ctx):
    await ctx.send(file=discord.File('encrypt.py'))

@client.command()
async def email_hack(ctx):
    await ctx.send(file=discord.File('emails.txt'))
    await ctx.send('Hacked emails were sent !')


@client.command()
async def password_email(ctx):
    await ctx.send(file=discord.File('passwords.txt'))
    await ctx.send('Hacked email passwords sent')


@client.command()
async def phone_number(ctx):
    await ctx.send(file=discord.File('phonenumbers.txt'))
    await ctx.send('The phone number registered in the hacked emails was sent')

client.run(config.token)
