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

from src.utils import logging
from src.utils.utils import sponsors, create_embed

class AutoCommands(commands.Cog, name="Auto Commands"):
	""" These commands will fire automatically.
	
	Arguments:
		bot {discord.Cog} -- The bot object.
	
	Commands:
		on_ready -- Fires when the bot is ready.
		on_member_join -- Fires when a member joins the server.
		on_member_remove -- Fires when a member leaves the server.
		on_command_error -- Fires when a command fails.
		on_message_delete -- Fires when a message is deleted.
		on_message_edit -- Fires when a message is edited.
	"""

	def __init__(self, bot):
		""" Init function for AutoCommands."""
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		""" This will run when the bot is ready. """
		activity = discord.Activity(type=discord.ActivityType.watching, name="Cybel | !help")
		await self.bot.change_presence(activity=activity)
		logging.info(f'{self.bot.user.name} is Online...')


	@commands.Cog.listener()
	async def on_member_join(self, member: discord.Member):
		""" This will fire when a new member joins the server."""
		channel = member.guild.system_channel
		if channel is not None:
			embed = create_embed(ctx=None, title="Welcome", description=f"welcome {member.mention}, Introduce yourself to community.")
			await channel.send(embed=embed)
			await member.send("welcome to the Server! introduce yourself in server.\nOfficial Server for Cybel help: https://discord.gg/JfbK3bS\nUse `!help` command to get started.")


	@commands.Cog.listener()
	async def on_member_remove(self, member: discord.Member):
		""" This event triggers when a member leaves the server."""
		channel = member.guild.system_channel
		if channel is not None:
			embed = create_embed(ctx=None, title="Good Bye", description=f"{member} has left the server.")
			await channel.send(embed=embed)

	
async def setup(bot: commands.Cog):
	await bot.add_cog(AutoCommands(bot))
