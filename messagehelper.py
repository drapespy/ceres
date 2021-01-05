import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'm.')

@client.event
async def on_ready():
    print('Bot is now Online!')

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')