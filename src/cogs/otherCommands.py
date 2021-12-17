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


class OtherCommands(commands.Cog, name="Other Commands for Users : Other Commands"):
	"""
		Other Commands: Other discord server commands

	Commands:
		- ping - get the latency of the bot
		- source - Get the source code of the bot
	"""

	def __init__(self, bot):
		self.bot = bot


	@commands.command(aliases=["test", "hi", "hello", "pong"], help="Get the ping of the bot")
	async def ping(self, ctx):
		"""
			Get the ping of the bot

		command: !ping

		**Usage**
			get the latency of the bot
		"""
		embed = discord.Embed(title="Pong 🏓", description="{} ms".format(round(self.bot.latency * 1000)), color=discord.Color.green())
		await ctx.send(embed=embed)


	@commands.command(aliases=["github", "source_code"], help="get the source code")
	async def source(self, ctx):
		""" get the bot source code

		command: !source

		**Usage**:
			`source`: Get the bot source code
		"""
		try:
			source_url = "https://github.com/codePerfectPlus/cybel"
			await ctx.send("The bot is powered by **Cybel**\n\n**Source Code**: {}\n\nDon't forget to star the repo if you like it!".format(source_url))
		except Exception as e:
			await ctx.send('```{} - {}```'.format(type(e).__name__, e))


def setup(bot: commands.Cog):
	bot.add_cog(OtherCommands(bot))
