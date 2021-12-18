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
import datetime
from better_profanity import profanity

from src.utils.dbhelper import DBHelper
from src.utils.utils import sponsors

class NsfwCommands(commands.Cog, name="command for NSFW: NSFW Commands"):
	""" NSFW commands 
	
	commands:
		- report - report a user
		- on_message - delete the message if it contains bad words
	"""

	def __init__(self, bot):
		self.bot = bot
		self.db = DBHelper()

	@commands.command(aliases=["report_user"], help="Report a user")
	async def report(self, ctx, reported_member:discord.Member, *reason):
		""" Report a user

		command: !report @user reason

		**Usage**:
			`report`: Report user for misbehavior, abuse, suspicious behaviour etc.
		"""
		try:
			reported_member = reported_member
			reported_by = ctx.author
			reported_to = ctx.guild.owner
			reason = ' '.join(reason)


			embed = discord.Embed(title="Report Status", color=discord.Color.red())
			embed.add_field(name="Reported User", value=reported_member, inline=False)
			embed.add_field(name="Reported By", value=reported_by.mention)
			embed.add_field(name="Reported to", value=reported_to.mention)
			embed.add_field(name="Reason", value=reason, inline=False)
			embed.set_author(name=reported_by, icon_url=reported_by.avatar_url)
			embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])


			self.db.create_report(datetime.datetime.utcnow().timestamp(),
				ctx.guild.id, reported_member.id, reported_by.id, reported_to.id, reason)
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.Cog.listener()
	async def on_message(self, message: discord.Message):
		''' 
		on_message event will fire when a message is sent.

		Arguments:
			message {discord.Message} -- The message object.

		'''

		if message.author.bot:
			return
		elif message.author.id == self.bot.user.id:
			return
		elif profanity.contains_profanity(message.content): # delete the message if it contains profanity
			await message.delete()
			await message.channel.send(f"**{message.author.mention}**, **Please do not use bad words!**")

		
def setup(bot: commands.Bot):
	bot.add_cog(NsfwCommands(bot))
