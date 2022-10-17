# -*- coding: utf-8 -*-
'''
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
'''
import asyncio
import discord
from discord import Intents
from discord.ext import commands

from src.utils import logging
from src.utils import DISCORD_TOKEN

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   case_insensitive=True,
                   description='''Cybel - A Powerfull, Advanced, and Open Source Discord Bot.\nGithub:-  [CodePerfectPlus](https://github.com/codeperfectoplus)\nDeveloper:  [Deepak Raj](https://www.linkedin.com/in/deepak-raj-35887386/)\nContact Email:- botcybel@gmail.com''')

        
cog_dict = {
    'Other Commands': 'src.cogs.otherCommands',
    'Auto Commands': 'src.cogs.autoCommands',
    'Admin Commands': 'src.cogs.adminCommands',
    'API Based Commands': 'src.cogs.apiBasedCommands',
    'Moderation Commands': 'src.cogs.moderationCommands',
    'NSFW Commands': 'src.cogs.nsfwCommands',
    'Fun Commands': 'src.cogs.funCommands',
    'Utility Commands': 'src.cogs.utilityCommands',
    'Music Commands': 'src.cogs.musicCommands', # FIXME: add music commands in future update
    'Owner Commands': 'src.cogs.ownerCommands',
    'Testing Commands': 'src.cogs.testingCommands',
    'Error Handler': 'src.cogs.errorHandler',
}

async def load_cogs(cog_dict: dict):
    """ Function for loading cogs using dictionary """
    try:
        for key, value in cog_dict.items():
            logging.info('Loading... {}'.format(key))
            await bot.load_extension(value)
    except Exception as e:
        logging.error('{} - {}'.format(type(e).__name__, e))


if __name__ == '__main__':
    asyncio.run(load_cogs(cog_dict=cog_dict))
    bot.run(DISCORD_TOKEN)
