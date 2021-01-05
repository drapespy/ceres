import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = 'm.')

@client.event
async def on_ready():
    print('Bot is now Online!')

@client.event
async def on_ready():
    activity = discord.Game(name="Deleting Messages", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.command()
async def ping(ctx):
    await ctx.send(f'The Bots ping is {round(client.latency * 1000)}ms')

@client.command()
async def embed(ctx):
    embed = discord.Embed(Title = "Test Embed")
    await ctx.send(embed=embed)

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')