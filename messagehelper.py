import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = 'm.')

@client.event
async def on_ready():
    activity = discord.(name="m.commands", type=3)
await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="m.commands"))
    print("Bot is ready!")

@client.command()
async def commands(ctx):
    await ctx.send('`m.commands` - Shows This Help Message\n`m.ping` - Shows the bots latency')

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping! MessageHelpers current ping is **{round(client.latency * 1000)}**ms')

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')