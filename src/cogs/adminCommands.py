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

	Commands:
		kick - Kick a user from the server.
		mute - Mute a user.
		unmute - Unmute a user.
		ban - Ban a user from the server.
		unban - Unban a user from the server.
		create_category - Create a category.
		delete_category - Delete a category.
		create_text_channel - Create a text channel.
		delete_text_channel - Delete a text channel.
		create_voice_channel - Create a voice channel.
		delete_voice_channel - Delete a voice channel.
		create_role - Create a role.
		delete_role - Delete a role.
		give_role - Give a role to a user.
		give_role_to_all - Give a role to all users.
		dm - Direct message a user.
		change_username - Change the username of bot
		change_avatar - Change the avatar of bot
		change_status - Change the status of bot
		change_game - Change the game of bot
		change_status_and_game - Change the status and game of bot
		change_nickname - Change the nickname of a user.

	"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
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
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
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
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
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
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
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
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
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
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def create_category(self, ctx, category: str):
		""" Command for create category in Guild/Server.

		command: !create_category <category_name>

		**Usage**:
			create category in guild/server.
			Cybel Need administrator access for create category.
		"""
		await ctx.guild.create_category(category)
		embed = discord.Embed(title="New Category Created", color=discord.Color.blue())
		embed.add_field(
			name="Created Category", value=category)
		embed.add_field(
			name="Created by", value=ctx.author.mention)
		embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def delete_category(self, ctx, category: discord.CategoryChannel):
		""" Command for delete category from server

		command: !delete_category <category_name>

		**Usage**:
			delete category from server.
			Cybel Need administrator access for delete category.
		"""
		await category.delete()
		embed = discord.Embed(title="Category Deleted", color=discord.Color.blue())
		embed.add_field(
			name="Deleted Category", value=category)
		embed.add_field(
			name="Deleted by", value=ctx.author.mention)
		embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def create_text_channel(self, ctx, channel: str, category: discord.CategoryChannel = None):
		""" command for create text channel in Guild/Server.

		command: !create_text_channel <channel_name> <category_name>

		**Usage**:
			create text channel in guild/server.
			Cybel Need administrator access for create text channel.

			it will not override the previous channel
			Category name is optional.

			for creating new category, please check !help create_category
			"""
		if category is None:
			await ctx.guild.create_text_channel(channel)
		else:
			await ctx.guild.create_text_channel(channel, category=category)
		embed = discord.Embed(
			description=f'{channel} got created by {ctx.author.mention}', color=discord.Color.blue())
		embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def delete_text_channel(self, ctx, channel: discord.TextChannel):
		""" Command for delete text channel

		command: !delete_text_channel <channel_name>

		**Usage**:
			delete text channel from server.
			Cybel Need administrator access for delete text channel.
		"""
		await channel.delete()
		embed = discord.Embed(title="Text Channel Deleted", color=discord.Color.blue())
		embed.add_field(
			name="Deleted Text Channel", value=channel)
		embed.add_field(
			name="Deleted By", value=ctx.author.mention)
		embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def create_voice_channel(self, ctx, channel: str, category: discord.CategoryChannel = None):
		""" command for create voice channel in Guild/Server

		command: !create_voice_channel <channel_name> <category_name>

		**Usage**:
			create voice channel in guild/server.
			Cybel Need administrator access for create voice channel.

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
		""" Command for delete voice channel

		command: !delete_voice_channel <channel_name>

		**Usage**:
			delete voice channel from server.
			Cybel Need administrator access for delete voice channel.
		"""
		await channel.delete()
		embed = discord.Embed(title= "Voice Channel Deleted", color=discord.Color.blue())
		embed.add_field(
			name="Deleted Voice Channel", value=channel)
		embed.add_field(
			name="Deleted By", value=ctx.author.mention)
		embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def create_role(self, ctx, *, new_role_name):
		""" Create New Roles in the Server

		command: !create_role <role_name>

		**Usage**:
			create new role in server.
			Cybel Need manage_roles permission for create new role.
		"""
		await ctx.guild.create_role(name=new_role_name)
		embed = discord.Embed(
			title="New Role Created", color=discord.Color.blue())
		embed.add_field(
			name="Role", value=new_role_name)
		embed.add_field(
			name="Approved by", value=ctx.author.mention)
		embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def delete_role(self, ctx, role: discord.Role):
		""" Command for delete role

		command: !delete_role <role_name>

		**Usage**:
			delete role from server.
			Cybel Need manage_roles permission for delete role.
		"""
		await role.delete()
		embed = discord.Embed(title="Role Deleted", color=discord.Color.blue())
		embed.add_field(
			name="Deleted Role", value=role)
		embed.add_field(
			name="Deleted by", value=ctx.author.mention)
		embed.set_thumbnail(
			url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def give_role(self, ctx, member: discord.Member, role: discord.Role):
		""" Give role to Server's members

		command: !give_role <member_name> <role_name>

		**Usage**:
			give role to server's members.
			Cybel Need manage_roles permission for give role.
		"""
		await member.add_roles(role)
		embed = discord.Embed(
			title="New Role Assigned", color=discord.Color.blue())
		embed.add_field(
			name="Member", value=member.mention)
		embed.add_field(
			name="New Role", value=role.name)
		embed.add_field(
			name="Assigned by", value=ctx.author.mention)
		embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
		embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)


	# REVIEW - : optimize code for instead making for loop and giving each one role
	@commands.command(hidden=True)
	@commands.has_permissions(manage_roles=True)
	async def give_roll_to_all(self, ctx, role: discord.Role):
		""" Give Roll to all members in once

		command: !give_roll_to_all <role_name>

		**Usage**:
			give role to all members in server.
			Cybel Need manage_roles permission for give role.
		"""
		try:
			for member in ctx.guild.members:
				await member.add_roles(role)
			await ctx.send(f"Giving {role} role to all members.")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def dm(self, ctx, member: discord.Member, *, message: str):
		""" Command for DM members in server

		command: !dm <member_name> <message>

		**Usage**:
			send message to member in server.
			Cybel Need administrator access for send message.
		"""
		try:
			await member.send(message)
			await ctx.send(f"DM sent to {member.mention}")
		except Exception as e:
			await ctx.send(f"{member.mention} have DMs disabled")


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def change_bot_username(self, ctx, *, new_username: str):
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


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def change_bot_avatar(self, ctx, *, new_avatar: str):
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


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def change_bot_status(self, ctx, *, new_status: str):
		""" Change status

		command: !status <new_status>

		**Usage**:
			change status of server.
			Cybel Need administrator permission for change status.
		"""
		try:
			await ctx.bot.change_presence(activity=discord.Game(name=new_status))
			await ctx.send(f"Status changed to {new_status}")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def change_bot_game(self, ctx, *, new_game: str):
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

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def change_bot_status_and_game(self, ctx, *, new_status_and_game: str):
		""" Change status and game

		command: !status_and_game <new_status_and_game>

		**Usage**:
			change status and game of server.
			Cybel Need administrator permission for change status and game.
		"""
		try:
			await ctx.bot.change_presence(activity=discord.Game(name=new_status_and_game))
			await ctx.send(f"Status and game changed to {new_status_and_game}")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def change_nickname(self, ctx, member: discord.Member, *, new_nickname: str):
		""" Change nickname

		command: !nickname <member_name> <new_nickname>

		**Usage**:
			change nickname of member.
			Cybel Need administrator permission for change nickname.
		"""
		try:
			await member.edit(nick=new_nickname)
			await ctx.send(f"Nickname changed to {new_nickname}")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


def setup(bot: commands.Cog):
	bot.add_cog(AdminCommands(bot))
