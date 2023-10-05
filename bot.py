# Import necessary libraries
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables from a .env file
load_dotenv()
# The intents
intents = discord.Intents.default()
intents.typing = True
# Set up the bot command prefix
bot = commands.Bot(command_prefix='/', intents=intents)

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
# End of hello

# About Kilifi scholarship
@bot.command(name='about', help='What Kilifi scholarship is about')
async def about(ctx):
    """What is the Kilifi County Scholarship program in partnership with the Power Learn Project?"""
    await ctx.send("The Kilifi County Scholarship program, in collaboration with the Power Learn Project, is an initiative aimed at providing students with access to quality online education and resources for software development studies.")
# End of about

# # LMS
# @bot.command(name='lms', help='LMS')
# async def lms(ctx):
#     """How will the online learning platform work?"""
#     await ctx.send("The online learning platform will provide students with access to a Learning Management System (LMS) where they can find course materials, assignments, and resources. Students will be able to study from the comfort of their own homes.")
# # End of LMS

# Requirements
@bot.command(name='requirements', help='Requirements')
async def requirements(ctx):
    """What are the prerequisites for participating in this scholarship program?"""
    await ctx.send("To participate, students are required to have their own gadgets (such as laptops or computers) and internet bundles for online learning.")
# End of Requirements

# Gadget
@bot.command(name='gadgets', help='Gadgets used')
async def gadgets(ctx):
    """What kind of gadget is recommended for online learning?"""
    await ctx.send("A laptop or computer with the specified system requirements is recommended to effectively engage in online courses and complete software development projects.")
# End of gadgets

# Financial support
@bot.command(name='bundles', help='Financial support')
async def bundles(ctx):
    """Is there financial support for purchasing a gadget or internet bundles?"""
    await ctx.send("Currently, the program does not provide financial support for gadgets or internet bundles. Students are responsible for ensuring they have the necessary equipment and internet access.")
# End of financial support

# Access LMS
@bot.command(name='lms', help='lms')
async def lms(ctx):
    """How can I get access to the Learning Management System (LMS) for course materials and resources?"""
    await ctx.send("Students will be onboarded onto the LMS, and login details will be provided to access course materials, assignments, and other resources.")
# End of LMS

# Classes
@bot.command(name='classes', help='Classes')
async def classes(ctx):
    """Will there be live virtual classes or recorded lectures?"""
    await ctx.send("The program may include a combination of live virtual classes, recorded lectures, and self-paced learning materials. Details about the format will be provided for each course.")
# End of Classes

# Contact
@bot.command(name='contact', help='Contact support')
async def contact(ctx):
    """How can I contact the program coordinators or support team if I have questions or need assistance?"""
    await ctx.send("Contact information for program coordinators and support staff will be provided to students. You can typically reach out via email or through designated communication channels.")
# End of Contact


# Goal
@bot.command(name='goal', help='Goal')
async def goal(ctx):
    """What is the goal of the Kilifi County Scholarship program?"""
    await ctx.send("The program's primary goal is to empower students in Kilifi County with software development skills and knowledge, preparing them for future career opportunities in the tech industry.")
# End of Goal

# Run the bot with your Discord bot token
bot.run(os.environ['DISCORD_BOT_TOKEN'])
