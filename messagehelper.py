import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = 'm.')

@client.event
async def on_ready():
    print('Bot is now Online!')

@client.command()
async def ping(ctx):
    await ctx.send(f'The Bots ping is {round(client.latency * 1000)}ms')

@client.command()
async def embed(ctx):
    embed = discord.Embed(Title = "Test Embed")

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')