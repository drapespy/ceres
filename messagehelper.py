import discord
from discord.ext import commands
import datetime
import asyncio

client = commands.Bot(command_prefix = 'm.')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="m.help | dsc.gg/xydev"))
    print("Bot is ready!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("<:error:798368255991087125> `That is not a valid command.`")

@client.command(aliases=['commands', 'cmds', 'cmnds', 'cmd', 'cmnd'])
async def help(ctx):
    embed=discord.Embed(title="", color=0x7289da)
    embed.add_field(name="m.help", value="Shows this message.", inline=False)
    embed.add_field(name="m.ping", value="Sends the bot's latency.", inline=True)
    embed.add_field(name="m.purge (num)", value="Deletes the given amount of messages.", inline=False)
    embed.set_footer(text="My prefix is m.")
    await ctx.send(embed=embed)

@client.command
async def bhunkymunky(ctx):
    await ctx.send('Subscribe to Bhunky Munky [here](https://www.youtube.com/channel/UCIN_VAFZhU6977tGmiVYlZg?sub_confirmation=1)')

@client.command(aliases=['clear'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['latency'])
async def ping(ctx):
  message = await ctx.send("`Pinging Server...`")
  await asyncio.sleep(1)
  await message.edit(content=f"MessageHelper's current ping is **{round(client.latency * 1000)}**ms")

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<:error:798368255991087125> `Please specify a number of messages to delete.`")

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')