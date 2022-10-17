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

from src.utils.dbhelper import DBHelper
from src.utils.utils import create_embed

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
			reported_by = ctx.author
			reported_to = ctx.guild.owner
			reason = ' '.join(reason)


			embed = create_embed(ctx, title="Report Status", color=discord.Color.red())
			embed.add_field(name="Reported User", value=reported_member.mention, inline=False)
			embed.add_field(name="Reported By", value=reported_by.mention)
			embed.add_field(name="Reported to", value=reported_to.mention)
			embed.add_field(name="Reason", value=reason, inline=False)
			reported_by = str(self.bot.get_user(reported_by.id))
			reported_to = str(self.bot.get_user(reported_to.id))
			reported_member = str(self.bot.get_user(reported_member.id))

			self.db.create_report(str(datetime.datetime.utcnow()),  # db function to create report
				ctx.guild.id, reported_member, reported_by, reported_to, reason)

			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

		
async def setup(bot: commands.Bot):
	await bot.add_cog(NsfwCommands(bot))
