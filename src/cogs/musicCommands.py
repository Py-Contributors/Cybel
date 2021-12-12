"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
"""
from discord.ext import commands
import discord


class MusicCommands(commands.Cog, name="Commands for music activity."):
    def __init__(self, bot):
        self.bot = bot


def setup(bot: commands.Cog):
    bot.add_cog(MusicCommands(bot))
