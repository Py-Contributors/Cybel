"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
"""
import discord
from discord.ext import commands

class OwnerCommands(commands.Cog, name="Commands for Bot Owner only (Developer)"):
	""" Testing commands """

	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(help="change the username of bot")  # change bot the
	@commands.is_owner()
	async def change_bot_username(self, ctx, new_username: str):
		""" Change username

		command: !username <new_username>

		**Usage**:
			change username of server.
			Cybel Need administrator permission for change username.
		"""
		try:
			await ctx.bot.user.edit(username=new_username)
			await ctx.send(f"Username changed to {new_username}")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command(help="change the avatar of bot")
	@commands.is_owner()
	async def change_bot_avatar(self, ctx, new_avatar: str):
		""" Change avatar of bot

		command: !avatar <new_avatar>

		**Usage**:
			change avatar of server.
			Cybel Need administrator permission for change avatar.
		"""
		try:
			await ctx.bot.user.edit(avatar=new_avatar)
			await ctx.send(f"Avatar changed to {new_avatar}")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command(help="change the bot status")
	@commands.is_owner()
	async def change_bot_game(self, ctx, new_game: str): # FIXME: Update dynamically from some api or something
		""" Change game

		command: !game <new_game>

		**Usage**:
			change game of server.
			Cybel Need administrator permission for change game.
		"""
		try:
			await ctx.bot.change_presence(activity=discord.Game(name=new_game))
			await ctx.send(f"Game changed to {new_game}")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')
		

def setup(bot: commands.Bot):
	bot.add_cog(OwnerCommands(bot))