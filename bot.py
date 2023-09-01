import discord
from discord.ext import commands

# Create a bot instance with intents
intents = discord.Intents.default()
intents.typing = False  # Disable typing events to reduce unnecessary data
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

# Bot's actual token
# bot.run('MTE0Njc4NDA2MTg4MTMzNTkzOA.GWox_K.dPHnK-h3-CKmjXozyyUczkHsJedmxTBykW0u84')
