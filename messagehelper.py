import discord
from discord.ext import commands
import datetime
import asyncio
import random
import json

client = commands.Bot(command_prefix = 'm.')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for m.help | v1.085"))
    print("Bot is ready!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("<:error:798368255991087125> `That is not a valid command.`")

@client.command(aliases=['commands', 'cmds', 'cmnds', 'cmd', 'cmnd'])
async def help(ctx):
    embed=discord.Embed(title="", color=0x7289da)
    embed.add_field(name="```m.help```", value="Shows this message.", inline=True)
    embed.add_field(name="```m.ping```", value="Sends the bot's latency.", inline=True)
    embed.add_field(name="```m.purge (num)```", value="Deletes the given amount of messages.", inline=False)
    embed.add_field(name="```m.lock```", value="Locks the current channel for @everyone.")
    embed.add_field(name="```m.unlock```", value="unlocks the current channel for @everyone.")
    await ctx.send(embed=embed)

@client.command()
async def bhunkymunky(ctx):
    embed=discord.Embed(title="Subscribe", description="Subscribe to Bhunky Munky [here](https://www.youtube.com/channel/UCIN_VAFZhU6977tGmiVYlZg?sub_confirmation=1)", color=0xff0000)
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/oUnPdbEjX1Lt3X8k9qpyWv7WtE85WJroh4vtYvPLI6E/https/yt3.ggpht.com/ytc/AAUvwniq8P1kPeEdA2UMTGyOgo4cof7ex9OFVGd19wMA%3Ds900-c-k-c0x00ffffff-no-rj?width=610&height=610")
    embed.set_footer(text="subscribe or die")
    await ctx.send(embed=embed)

@client.command(aliases=['close'])
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('🔐 Channel locked.')

@client.command(aliases=['open'])
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('🔓 Channel unlocked.')

@client.command(aliases=['clear'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def penis(ctx):
    await ctx.send("penids\nhttps://tenor.com/view/penis-music-gif-17978040")

@client.command(aliases=['latency'])
async def ping(ctx):
    message = await ctx.send("`Pinging Server...`")
    await asyncio.sleep(1)
    await message.edit(content=f"MessageHelper's latency is **{round(client.latency * 1000)}**ms")

@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("<:error:798368255991087125> `Missing required permissions. (Manage Channels)`")

@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("<:error:798368255991087125> `Missing required permissions. (Manage Channels).`")

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<:error:798368255991087125> `Please specify a number of messages to delete.`")

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')