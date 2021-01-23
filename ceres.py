import discord
from discord.ext import commands
import datetime
import asyncio
import random
import json
import os

client = commands.Bot(command_prefix = 'c.')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} guilds | c.help"))  
    print("Bot is ready!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("<:error:798368255991087125> `That is not a valid command.`")

@client.command(aliases=['commands', 'cmds', 'cmnds', 'cmd', 'cmnd'])
async def help(ctx):
    embed=discord.Embed(title="", color=0x7289da)
    embed.add_field(name="```c.help```", value="Shows this message.", inline=True)
    embed.add_field(name="```c.ping```", value="Sends the bot's latency.", inline=True)
    embed.add_field(name="```c.aliases```", value="Shows the command aliases.", inline=True)
    embed.add_field(name="```c.purge (num)```", value="Deletes the given amount of messages.", inline=True)
    embed.add_field(name="```c.slowmode```", value="Sets the slowmode of the channel.", inline=False)
    embed.add_field(name="```c.lock```", value="Locks the current channel for @everyone.", inline=True)
    embed.add_field(name="```c.unlock```", value="unlocks the current channel for @everyone.", inline=True)
    await ctx.send(embed=embed)

@client.command()
async def bhunkymunky(ctx):
    embed=discord.Embed(title="Subscribe", description="Subscribe to Bhunky Munky [here](https://www.youtube.com/channel/UCIN_VAFZhU6977tGmiVYlZg?sub_confirmation=1)", color=0xff0000)
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/oUnPdbEjX1Lt3X8k9qpyWv7WtE85WJroh4vtYvPLI6E/https/yt3.ggpht.com/ytc/AAUvwniq8P1kPeEdA2UMTGyOgo4cof7ex9OFVGd19wMA%3Ds900-c-k-c0x00ffffff-no-rj?width=610&height=610")
    embed.set_footer(text="subscribe or not cool monke")
    await ctx.send(embed=embed)

@client.command(aliases=['morgzmum'])
async def morgz(ctx):
    embed=discord.Embed(title="Morgz Mum", description="Subscribe to Morgz Mum [here](https://www.youtube.com/channel/UCqsUQhA6UIwSams54bEnCJw?sub_confirmation=1)", color=0xff0000)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AAUvwngshFr8zwbVJ5Tv8i9ZpaL11LFqlwX6DTHKoh_D=s88-c-k-c0x00ffffff-no-rj")
    embed.set_footer(text="subscribe or not true morgz fan")
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
    if amount > 100:
        await ctx.send("<:error:798368255991087125> `Limit = 100`")
        return
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['sm'])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"<a:success:799436964406755329> Set the slowmode in this channel to `{seconds}` seconds!")

@client.command()
async def penis(ctx):
    await ctx.send("penids\nhttps://tenor.com/view/penis-music-gif-17978040")

@client.command(aliases=['latency'])
async def ping(ctx):
    message = await ctx.send("`Pinging Server...`")
    await asyncio.sleep(1)
    await message.edit(content=f"Ceres' latency is **{round(client.latency * 1000)}**ms")

@client.command()
async def aliases(ctx):
    embed=discord.Embed(title="Command Aliases", color=0x7289da)
    embed.add_field(name="```c.help```", value="commands, cmd, cmds, cmnd, cmnds", inline=False)
    embed.add_field(name="```c.ping```", value="latency", inline=False)
    embed.add_field(name="```c.purge```", value="clear", inline=False)
    embed.add_field(name="```c.slowmode```", value="sm", inline=False)
    embed.add_field(name="```c.lock```", value="close", inline=False)
    embed.add_field(name="```c.unlock```", value="open", inline=False)
    await ctx.send(embed=embed)

@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("<:error:798368255991087125> `Missing required permissions: Manage Channels`")

@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("<:error:798368255991087125> `Missing required permissions: Manage Channels`")

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<:error:798368255991087125> `Please specify a number of messages to delete.`")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("<:error:798368255991087125> `Missing required permissions: Manage Messages`")

@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<:error:798368255991087125> `Please specify a number of seconds to set the slowmode to.`")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("<:error:798368255991087125> `Missing required permissions: Manage Channels`")

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')