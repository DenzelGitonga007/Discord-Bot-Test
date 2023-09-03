# Import necessary libraries
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables from a .env file
load_dotenv()
# The intents
intents = discord.Intents.default()
intents.typing = False
# Set up the bot command prefix
bot = commands.Bot(command_prefix='', intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print("Bot '{}' is online...".format(bot.user.name))

# Event handler for when a message is received
@bot.event
async def on_message(message):
    # Convert the message content to lowercase
    message.content = message.content.lower()
    
    # Process the message as needed
    await bot.process_commands(message)

# Responds to !hello
@bot.command(name='hello', help='Say hello to the bot')
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.author.mention))

# Run the bot with your Discord bot token
bot.run(os.environ['DISCORD_BOT_TOKEN'])
