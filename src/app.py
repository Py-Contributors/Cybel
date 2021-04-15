"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:- https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=268446835&scope=bot

"""
import os
import random
import discord
from discord import Intents
from discord.ext import commands
import requests

print(f'Discord Version : {discord.__version__}')

TOKEN = os.environ.get('DISCORD_TOKEN')

intents = Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """ Change Bot Presense """
    print(f'{bot.user.name} is Online...')

@bot.command()
async def ping(ctx):
	""" A Ping Pong function """
	await ctx.send('Pong!')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together. !add 5 5"""
    await ctx.send(left + right)

@bot.command()
async def quote(ctx):
	""" function to send random quote """
	try:
		randomQuoteURL = 'https://zenquotes.io/api/random'
		response = requests.get(randomQuoteURL)
		randomQuote = f'{response.json()[0]["q"]} - **{response.json()[0]["a"]}**'
		await ctx.send(randomQuote)
	except Exception as error:
		await ctx.send(error)

@bot.command()
async def joke(ctx):
	""" function to send random joke """
	try:
		randomJokeURL = 'https://v2.jokeapi.dev/joke/Any?type=single'
		randomJoke = requests.get(randomJokeURL)
		await ctx.send(randomJoke.json()['joke'])
	except Exception as error:
		await ctx.send(error)

@bot.command()
async def fact(ctx):
	""" function to send random fact """
	try:
		randomFactURL = 'https://uselessfacts.jsph.pl//random.json?language=en'
		randomFact = requests.get(randomFactURL)
		await ctx.send(randomFact.json()['text'])
	except Exception as error:
		await ctx.send(error)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.event
async def on_member_join(member):
    await member.send('Private message')

bot.run(TOKEN)
