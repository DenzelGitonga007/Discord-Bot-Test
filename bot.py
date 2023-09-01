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

# Replace 'YOUR_TOKEN_HERE' with your bot's actual token
bot.run('MTE0Njc4NDA2MTg4MTMzNTkzOA.GG35Rb.-iN7pkmvT7utZxDufEmP470aQ50opI1e8PxGUU')
