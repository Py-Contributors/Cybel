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


class AdminCommands(commands.Cog, name="Commands for Server Management: Admin Commands"):
	""" Admin Level Commands

	Some commands May Require administrator access.
	"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		""" command to kick user

		command: !kick <member_name> <reason_to_kick>
		output: function will remove user from server with embed message.
		"""
		await ctx.message.delete()
		try:
			await member.kick(reason=reason)
			kick = discord.Embed(title=f"Kicked {member.name}!")
			kick.add_field(
				name="Kicked Member :boot:", value=member.name)
			kick.add_field(
				name="Kicked By", value=ctx.author.mention)
			kick.add_field(
				name="Reason for kick", value=reason)
			kick.set_thumbnail(
            	url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			await ctx.send(embed=kick)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def mute(self, ctx, member: discord.Member):
		""" Mute the user for voice activity

		command: !mute <member_name>
		output: It will mute the voice channel connected memeber.
		user should be connected to the voice channel.

		Cybel Need administrator access for mute command.
		"""
		await ctx.message.delete()
		try:
			await member.edit(mute=True)
			mute = discord.Embed(title=f"Muted {member.name}")
			mute.add_field(
				name="Muted Member :mute:", value=member.mention)
			mute.add_field(
				name="Muted By", value=ctx.author.mention)
			mute.set_thumbnail(
            	url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			await ctx.send(embed=mute)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def unmute(self, ctx, member: discord.Member):
		""" Unmute the user for voice activity

		command: !unmute <member_name>
		output: It will unmute the voice channel connected memeber.

		Cybel Need administrator access for mute command.
		"""
		await ctx.message.delete()
		try:
			await member.edit(unmute=True)
			unmute = discord.Embed(title=f"Unuted {member.name}")
			unmute.add_field(
				name="Unmuted Member :loud_sound:", value=member.mention)
			unmute.add_field(
				name="Unmuted By", value=ctx.author.mention)
			unmute.set_thumbnail(
            	url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			await ctx.send(embed=unmute)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		""" command to ban user

		command: !ban <member> <reason>
		Cybel Need ban_members access for ban command.
		"""
		await ctx.message.delete()
		try:
			await member.ban(reason=reason)
			ban = discord.Embed(title=f"Banned {member.name}!")
			ban.add_field(
				name="Banned Member :boom:", value=member.name)
			ban.add_field(
				name="Banned By", value=ctx.author.mention)
			ban.add_field(
				name="Reason for Ban", value=reason)
			ban.set_thumbnail(
            	url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			await ctx.send(embed=ban)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def unban(self, ctx, *, member_id: int):
		""" command to unban user.

		command: !unban <member_id>
		Cybel Need administrator access for Unban command.
		"""
		await ctx.message.delete()
		try:
			await ctx.guild.unban(discord.Object(id=member_id))
			await ctx.send(f"Unban {member_id}")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
	@commands.has_permissions(manage_nicknames=True)
	async def chnick(self, ctx, member: discord.Member, nick):
		""" Change nicknames of the servers'members

		command: !chnick <member> <new_nickname>
		Cybel Need administrator access for change Nicknames.
		"""
		await ctx.message.delete()
		try:
			await member.edit(nick=nick)
			nickname = discord.Embed(title="Nickname Changed")
			nickname.add_field(
				name="Member", value=member.mention)
			nickname.add_field(
				name="Nickname Changed by", value=ctx.author.mention)
			nickname.set_thumbnail(
            	url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			await ctx.send(embed=nickname)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def create_category(self, ctx, category: str):
		""" Command for create category in Guild/Server.

		it will not override the previous category.
		"""
		await ctx.guild.create_category(category)
		category_embed = discord.Embed(title="New Category Created")
		category_embed.add_field(
			name="Created Category", value=category)
		category_embed.add_field(
			name="Created by", value=ctx.author.mention)
		category_embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		await ctx.send(embed=category_embed)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def delete_category(self, ctx, category: discord.CategoryChannel):
		""" Command for delete category from server """
		await category.delete()
		category_embed = discord.Embed(title="Category Deleted")
		category_embed.add_field(
			name="Deleted Category", value=category)
		category_embed.add_field(
			name="Deleted by", value=ctx.author.mention)
		category_embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		await ctx.send(embed=category_embed)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def create_text_channel(self, ctx, channel: str, category: discord.CategoryChannel = None):
		""" command for create text channel in Guild/Server.

		input: channel, category name

		it will not override the previous channel
		Category name is optional.

		for creating new category, please check !help create_category
		"""
		if category is None:
			await ctx.guild.create_text_channel(channel)
		else:
			await ctx.guild.create_text_channel(channel, category=category)
		txt_channel = discord.Embed(
			description=f'{channel} got created by {ctx.author.mention}')
		await ctx.send(embed=txt_channel)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def delete_text_channel(self, ctx, channel: discord.TextChannel):
		""" Command for delete text channel """
		await channel.delete()
		dlt_text_channel = discord.Embed(title="Text Channel Deleted")
		dlt_text_channel.add_field(
			name="Deleted Text Channel", value=channel)
		dlt_text_channel.add_field(
			name="Deleted By", value=ctx.author.mention)
		dlt_text_channel.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		await ctx.send(embed=dlt_text_channel)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def create_voice_channel(self, ctx, channel: str, category: discord.CategoryChannel = None):
		""" command for create voice channel in Guild/Server

		input: channel, category name

		it will not override the previous channel
		Category name is optional.

		for creating new category, please check !help create_category
		"""
		if category is None:
			await ctx.guild.create_voice_channel(channel)
		else:
			await ctx.guild.create_voice_channel(channel, category=category)
		voice_channel = f'{channel} got created by {ctx.author.mention}'
		await ctx.send(voice_channel)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def delete_voice_channel(self, ctx, channel: discord.VoiceChannel):
		""" Command for delete voice channel """
		await channel.delete()
		voice_channel = discord.Embed(title= "Voice Channel Deleted")
		voice_channel.add_field(
			name="Deleted Voice Channel", value=channel)
		voice_channel.add_field(
			name="Deleted By", value=ctx.author.mention)
		voice_channel.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		await ctx.send(embed=voice_channel)

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def create_role(self, ctx, *, new_role_name):
		""" Create New Roles in the Server

		Command Usage: !make_role MOD
		"""
		await ctx.guild.create_role(name=new_role_name)
		new_role_embed = discord.Embed(
			title="New Role Created")
		new_role_embed.add_field(
			name="Role", value=new_role_name)
		new_role_embed.add_field(
			name="Approved by", value=ctx.author.mention)
		new_role_embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		await ctx.send(embed=new_role_embed)

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def give_role(self, ctx, member: discord.Member, role: discord.Role):
		""" Give role to Server's members

		Commands Usage: !give_role <username>
		"""
		await member.add_roles(role)
		role_embed = discord.Embed(
			title="New Role Assigned")
		role_embed.add_field(
			name="Member", value=member.mention)
		role_embed.add_field(
			name="New Role", value=role.name)
		role_embed.add_field(
			name="Assigned by", value=ctx.author.mention)
		role_embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		await ctx.send(embed=role_embed)

	# FIXME - : optimize code for instead making for loop and giving each one role
	@commands.command(hidden=True)
	@commands.has_permissions(manage_roles=True)
	async def give_roll_to_all(self, ctx, role: discord.Role):
		""" Give Roll to all members in once """
		try:
			for member in ctx.guild.members:
				await member.add_roles(role)
				print(member)
			await ctx.send(f"Giving {role} role to all members.")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


def setup(bot: commands.Cog):
	bot.add_cog(AdminCommands(bot))
