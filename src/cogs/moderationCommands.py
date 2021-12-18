"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
"""
import os
from discord.ext import commands
import discord

from src.utils.dbhelper import DBHelper
from src.utils.utils import sponsors, root_dir

class ModerationCommands(commands.Cog, name="commands for server moderators: Moderation Commands"):
	"""
	
	Commands for moderation

	commands:
		kick - kicks a user
		mute - mutes a user
		unmute - unmute a user
		ban - bans a user
		unban - unban a user
	"""

	def __init__(self, bot):
		self.bot = bot
		self.db = DBHelper()
	

	@commands.command(aliases=["kick_member"], help="Kick a user from the server.")
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		""" command to kick user

		command: !kick @member <reason_to_kick>

		**Usage**:
		   kick @member for spamming, flooding, suspected hacking etc.

		"""
		await ctx.message.delete()
		try:
			await member.kick(reason=reason)
			embed = discord.Embed(title=f"Kicked {member.name}!", color=discord.Color.blue())
			embed.add_field(
				name="Kicked Member :boot:", value=member.name)
			embed.add_field(
				name="Kicked By", value=ctx.author.mention)
			embed.add_field(
				name="Reason for kick", value=reason)
			embed.set_thumbnail(
				url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))


	@commands.command(aliases=["mute_member"], help="Mute a user from voice channel")
	@commands.has_permissions(kick_members=True)
	async def mute(self, ctx, member: discord.Member):
		""" Mute the user for voice activity

		command: !mute @member

		**Usage**:
		   mute @member

		   It will mute the voice channel connected member.
			user should be connected to the voice channel.

			Cybel Need administrator access for mute command.


		"""
		await ctx.message.delete()
		try:
			await member.edit(mute=True)
			embed = discord.Embed(title=f"Muted {member.name}", color=discord.Color.blue())
			embed.add_field(
				name="Muted Member :mute:", value=member.mention)
			embed.add_field(
				name="Muted By", value=ctx.author.mention)
			embed.set_thumbnail(
				url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))

	@commands.command(aliases=["unmute_member"], help="Unmute a user from voice channel")
	@commands.has_permissions(kick_members=True)
	async def unmute(self, ctx, member: discord.Member):
		""" Unmute the user for voice activity

		command: !unmute @member

		**Usage**:
			It will unmute the voice channel connected member.
			Cybel Need administrator access for mute command.
		"""
		await ctx.message.delete()
		try:
			await member.edit(unmute=True)
			embed = discord.Embed(title=f"Unuted {member.name}", color=discord.Color.blue())
			embed.add_field(
				name="Unmuted Member :loud_sound:", value=member.mention)
			embed.add_field(
				name="Unmuted By", value=ctx.author.mention)
			embed.set_thumbnail(
				url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))


	@commands.command(aliases=["ban_member"], help="Ban a user from the server.")
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		""" command to ban user

		command: !ban @member <reason>

		**Usage**:
		   ban @member for spamming, flooding, suspected hacking etc.
			Cybel Need ban_members access for ban command.
		"""
		await ctx.message.delete()
		try:
			await member.ban(reason=reason)
			embed = discord.Embed(title=f"Banned {member.name}!", color=discord.Color.blue())
			embed.add_field(
				name="Banned Member :boom:", value=member.name)
			embed.add_field(
				name="Banned By", value=ctx.author.mention)
			embed.add_field(
				name="Reason for Ban", value=reason)
			embed.set_thumbnail(
				url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))

	@commands.command(aliases=["unban_member"], help="Unban a user from the server.")
	@commands.has_permissions(administrator=True)
	async def unban(self, ctx, *, member_id: int):
		""" command to unban user.

		command: !unban <member_id>

		**Usage**:
		   unban @member/ @member_id
			Cybel Need administrator access for Unban command.
		"""
		await ctx.message.delete()
		try:
			await ctx.guild.unban(discord.Object(id=member_id))
			await ctx.send(f"Unban {member_id}")
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))


	@commands.command(help="get the user's report csv")
	@commands.has_permissions(administrator=True)
	async def get_user_report(self, ctx, member: discord.Member):
		""" Get report of member

		command: !get_report <member_name>

		**Usage**:
			get report of member in csv
			Cybel Need administrator permission for get report.
		"""
		try:
		
			member = str(self.bot.get_user(member.id))
			
			df = self.db.get_report_csv("reported_user='{}'".format(member)) # db function to get report
			temp_file = os.path.join(root_dir, "logs", "temp.csv")  # temp file to save report
			df.to_csv(temp_file)
			await ctx.send(file=discord.File(temp_file))
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command(help="get the all reports from the server in csv")
	@commands.has_permissions(administrator=True)
	async def get_all_report(self, ctx):
		""" get all the reports from the server.

		command: !get_report <member_name>

		**Usage**:
			get report of member in csv
			Cybel Need administrator permission for get report.
		"""
		try:
		
			channel_id = ctx.guild.id
			df = self.db.get_report_csv("channel_id='{}'".format(channel_id)) # db function to get report
			temp_file = os.path.join(root_dir, "logs", "temp.csv")  # temp file to save report
			df.to_csv(temp_file)
			await ctx.send(file=discord.File(temp_file))
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')
	

	@commands.command(help="count the total number of report for single user")
	@commands.has_permissions(administrator=True)
	async def count_report(self, ctx, member: discord.Member):
		""" count number of report on user
		
		command: !count_report <member_name>

		**Usage**:
			count number of report on user
			Cybel Need administrator permission for count report.
		"""
		try:
			member = str(self.bot.get_user(member.id))
			count = self.db.get_report_count("reported_user='{}'".format(member))
			embed = discord.Embed(title="Report count", description="{} has {} reports".format(member, count), color=0x00ff00)
			embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
			embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command(help="count the total numbers of reports in guild")
	@commands.has_permissions(administrator=True)
	async def count_reports(self, ctx):
		""" count number of report on user
		
		command: !count_report <member_name>

		**Usage**:
			count number of report on user
			Cybel Need administrator permission for count report.
		"""
		try:
			channel_id = ctx.guild.id
			channel_name = ctx.guild.name
			count = self.db.get_report_count("channel_id='{}'".format(channel_id))
	

			embed = discord.Embed(title="Report count", color=0x00ff00)
			embed.add_field(name="Channel Name", value=channel_name, inline=False)
			embed.add_field(name="status", value="{} has total {} reports in server.".format(channel_name, count))
			embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
			embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command(help="delete user's report")	
	@commands.has_permissions(administrator=True)
	async def delete_report(self, ctx, member: discord.Member):
		""" Delete report of member

		command: !delete_report <member_name>

		**Usage**:
			delete report of member
			Cybel Need administrator permission for delete report.
		"""
		try:
			member = str(self.bot.get_user(member.id))
			channel_id = ctx.guild.id
			self.db.delete_user_report("reported_user='{}' AND channel_id={}".format(member, channel_id))
			embed = discord.Embed(title="Report deleted", description="{}'s report has been deleted.".format(member), color=0x00ff00)
			embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
			embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


def setup(bot: commands.Bot):
	bot.add_cog(ModerationCommands(bot))