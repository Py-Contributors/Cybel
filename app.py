# -*- coding: utf-8 -*-
'''
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
'''

from discord import Intents
from discord.ext import commands

from src.utils import logging
from src.utils import DISCORD_TOKEN

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   case_insensitive=True)

cog_dict = {
    'Auto Commands': 'src.cogs.autoCommands',
    'Admin Commands': 'src.cogs.adminCommands',
    'API Based Commands': 'src.cogs.apiBasedCommands',
    'Other Commands': 'src.cogs.otherCommands',
    #'Music Commands': 'src.cogs.musicCommands', # FIXME: Music Commands are not working

}

def load_cogs(cog_dict: dict):
    """ Function for loading cogs using dictionary """
    try:
        for key, value in cog_dict.items():
            logging.info(f'Loading... {key}')
            bot.load_extension(value)
    except Exception as e:
        logging.error(f'{type(e).__name__} - {e}')


if __name__ == '__main__':
    load_cogs(cog_dict)
    bot.run(DISCORD_TOKEN)
