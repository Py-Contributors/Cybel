"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
"""

import os
import discord
import aiohttp
from dotenv import load_dotenv
import logging
from pathlib import Path

bot_version = '2.0.0'

root_dir = Path(__file__).parent.parent.parent

load_dotenv()
logging.basicConfig(format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
                    encoding="utf-8",
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    handlers=[
                        logging.FileHandler(os.path.join(root_dir, 'logs', 'bot.log')),
                        logging.StreamHandler()])

logging.info(f'Discord Version : {discord.__version__}')


def get_environment_variable(key: str):
    """ Get the Environment variables

    DISCORD BOT TOKEN:- https://discord.com/developers/applications/
    OPENWEATHER API KEY:- https://openweathermap.org/
    """
    value = os.environ.get(key)
    try:
        if value is not None:
            logging.info('Loading... {}'.format(key))
            return value
        else:
            logging.error('{} is not found in environment variable.'.format(key))
    except Exception as e:
        logging.critical('Error while reading environment variables: {}'.format(e))


DISCORD_TOKEN = get_environment_variable('DISCORD_TOKEN')
WEATHER_API_KEY = get_environment_variable('WEATHER_API_KEY')
DATABASE_URL = get_environment_variable('DATABASE_URL')


async def _fetch(url: str):
    """ function to fetch data from api in asynchronous way """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()

# Weather image list used in weather embed to send random image
weather_image_list = [
    'https://cdn.discordapp.com/attachments/831943037936467985/834165838545551380/image.jpg',
    'https://cdn.discordapp.com/attachments/831943037936467985/834166839264149504/2019mexicoweather-forecast-v02.jpg',
    'https://cdn.discordapp.com/attachments/831943037936467985/834166849309769758/Austria2020weather-forecast-v02.jpg',
    'https://cdn.discordapp.com/attachments/831943037936467985/834166850169471067/Germany_weather.jpg',
    'https://cdn.discordapp.com/attachments/831943037936467985/834166848202735657/image_2.jpg',
    'https://cdn.discordapp.com/attachments/831943037936467985/834166848404324379/image_1.jpg',
    'https://cdn.discordapp.com/attachments/831943037936467985/834166851226304552/image_3.jpg']


def create_embed(ctx=None, title=None, description="", color=None):
    """ Create an embed with the given title, description and color

    Args:
        title (str): The title of the embed
        description (str): The description of the embed
        color (int): The color of the embed

    Returns:
        embed (discord.Embed): The embed created
    """
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
    if ctx is not None:
        embed.set_author(name=ctx.author.name)
    return embed
