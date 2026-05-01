import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Streaming(name='streaming-name', url='https://www.twitch.tv/urtwitchusername'))

bot.run('MTQ5OTczMjcxNzk2ODAzNTk3Mg.GjrNKe.fhRll2JXTUgxYo0ApKNrr4dgPqw4ZEqePq01Co')
