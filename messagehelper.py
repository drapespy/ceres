import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = 'm.')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="m.help | dsc.gg/xydev"))
    print("Bot is ready!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(':x: That is not a valid command')

@client.command()
async def help(ctx):
    await ctx.send('**__Stats__**\n`m.help` - Shows This Help Message\n`m.ping` - Shows the bots latency\n**__Messages__**\n`m.purge <amount>` - Clears the given amount of messages!')

@client.command(aliases=['clear'])
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):
    await ctx.send(f"`Pinging...`\nMessageHelper's current ping is **{round(client.latency * 1000)}**ms")

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(':x: Please specify a number of messages to delete.')

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')