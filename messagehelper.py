import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = 'm.')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="m.help | dsc.gg/xydev"))
    print("Bot is ready!")


@client.command()
async def help(ctx):
    await ctx.send('`m.help` - Shows This Help Message\n`m.ping` - Shows the bots latency')

@client.command()
async def ping(ctx):
    await ctx.send(f"`Pinging...`\nMessageHelper's current ping is **{round(client.latency * 1000)}**ms")

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')