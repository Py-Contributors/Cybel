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
			embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
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
			embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
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
			embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
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
			embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
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


def setup(bot: commands.Bot):
	bot.add_cog(ModerationCommands(bot))