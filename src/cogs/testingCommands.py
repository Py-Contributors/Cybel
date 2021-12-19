"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
"""

from discord.ext import commands

class TestingCommands(commands.Cog, name="testing command for server: Testing Commands"):
	""" Testing commands """

	def __init__(self, bot):
		self.bot = bot
	

def setup(bot: commands.Bot):
	bot.add_cog(TestingCommands(bot))