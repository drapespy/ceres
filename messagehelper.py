import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = 'm.')

@client.event
async def on_ready():
    print('Bot is now updated.')

@client.event
async def on_ready():
    activity = discord.Game(name="m.help", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.command()
async def help(ctx):
    await ctx.send('`m.help` - Shows This Help Message\n`m.ping` - Shows the bots latency')

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping! MessageHelpers current ping is **{round(client.latency * 1000)}**ms')

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')