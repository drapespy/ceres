import discord
from discord.ext import commands
import datetime
import asyncio

client = commands.Bot(command_prefix = 'm.')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Realease 40"))
    print("Bot is ready!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(':x: That is not a valid command')

@client.command(aliases=['commands'])
async def help(ctx):
    embed = discord.Embed(title = "Help" , color = 0x7289DA )
    embed.add_field(name= f"m.help" , value= "```Shows this message. ```" , inline=true)
    embed.add_field(name= f"m.ping" , value= "```Sends the latency of the bot.```" , inline=true)
    await ctx.send(embed=embed)

@client.command(aliases=['clear'])
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):
  message = await ctx.send("`Pinging...`")
  await asyncio.sleep(1)
  await message.edit(content=f"MessageHelper's current ping is **{round(client.latency * 1000)}**ms")

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(':x: Please specify a number of messages to delete.')

client.run('Nzg0MTY2MDE0NDc2NjE1Njkx.X8lVgg.f62CYt-37qsOxiihDM828TXuawM')