from distutils import command
import discord
import asyncio
from discord.ext import commands

bot = command.Bot(command_prefix='$')

@bot.command()
async def ban_time(ctx, member : command.MemberConverter):
    await ctx.guild.ban(member)
    await ctx.send(f'{member}')

bot.run('OTQ4NTMxNjY0NDc1Mjc1Mjk0.Yh9K8w.gtBlK2B-ZWz1KzEwPbhDRHyE92Y')