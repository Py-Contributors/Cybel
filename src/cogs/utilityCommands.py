'''
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
'''
from dataclasses import dataclass
from datetime import datetime
from discord.ext import commands
import discord

from src.utils.utils import bot_version, sponsors
from src.utils.dbhelper import DBHelper

class UtilityCommands(commands.Cog, name='Useful Commands for Users : Utility Commands'):
	''' Utility Commands 
	
	commands:
		- server_invite - Returns invite link for the server
		- bot_invite - Returns invite link for the bot
		- server_icon - Returns icon of the server
		- server_name - Returns name of the server
		- server_id - Returns id of the server
		- server_owner - Returns owner of the server
		- server_id - Returns id of the server
		- server_info - Returns info of the server
		- member_info - Returns info of the member
		- info_bot - Returns info of the bot
		- member_count - Returns member count of the server
		- get_avatar - Returns avatar of the member
		- get_user - Returns user info
	'''

	def __init__(self, bot):
		self.bot = bot
		self.db = DBHelper()


	@commands.command(aliases=['server_link'], help='Create an invite link for the server')
	async def server_invite(self, ctx):
		''' Create instant invite for Channel

		command: !create_invite

		**Usage**:
			`server_invite`: Create an invite link for the bot

		'''
		link = await ctx.channel.create_invite(unique=True)
		embed = discord.Embed(title="Invite Link", description="🔗", color=discord.Color.green())
		embed.add_field(name="Invite Link", value=link)
		embed.set_thumbnail(url=self.bot.user.avatar_url)
		embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
		embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])
		await ctx.send(embed=embed)


	@commands.command(aliases=['bot_invite', 'bot_link'], help='Get the invite link of the bot')
	async def invite_bot(self, ctx):
		''' Get invite link for bot

		command: !bot_invite

		**Usage**:
			`bot_invite`: Get the invite link of the bot
		'''
		# FIXME: generate bot invite dynamically
		link = 'https://top.gg/bot/832137823309004800/invite'
		embed = discord.Embed(title="Invite Link", description="🔗", color=discord.Color.green())
		embed.add_field(name="Invite Link", value=link)
		embed.set_thumbnail(url=self.bot.user.avatar_url)
		embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
		embed.set_footer(text="Sponsor by  {}".format(sponsors["name"]), icon_url=sponsors["icon"])
		await ctx.send(embed=embed)


	@commands.command(aliases=['icon'], help='get the server icon')
	async def server_icon(self, ctx):
		''' Get the server icon

		command: !server_icon

		**Usage**:
			`server_icon`: Get the server icon
		'''
		try:
			embed = discord.Embed(title='Server Icon', color=discord.Color.blue())
			embed.set_image(url=ctx.guild.icon_url)
			embed.set_thumbnail(url=self.bot.user.avatar_url)
			embed.add_field(name='Server Icon URL', value=ctx.guild.icon_url, inline=False)
			embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
			embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))


	@commands.command(help='get the server name')
	async def server_name(self, ctx):
		''' Get the server name

		command: !server_name

		**Usage**:
			`server_name`: Get the server name
		'''
		try:
			embed = discord.Embed(title='Server Information', color=discord.Color.blue())
			embed.set_thumbnail(url=self.bot.user.avatar_url)
			embed.add_field(name='Server Name', value=ctx.guild.name, inline=False)
			embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
			embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))


	@commands.command(help='get the server owner')
	async def server_owner(self, ctx):
		''' Get the server owner

		command: !server_owner

		**Usage**:
			`server_owner`: Get the server owner
		'''
		try:
			embed = discord.Embed(title='Server Information', color=discord.Color.blue())
			embed.set_thumbnail(url=self.bot.user.avatar_url)
			embed.add_field(name='Server Owner', value=ctx.guild.owner.mention, inline=False)
			embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
			embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))


	@commands.command(help='get the server id')
	async def server_id(self, ctx):
		''' Get the server id

		command: !server_id

		**Usage**:
			`server_id`: Get the server id
		'''
		try:
			embed = discord.Embed(title='Server Information', color=discord.Color.blue())
			embed.set_thumbnail(url=self.bot.user.avatar_url)
			embed.add_field(name='Server ID', value=ctx.guild.id, inline=False)
			embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
			embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))
	
	@commands.command(name='server_info', help='Get information about the discord server')
	async def server_info(self, ctx):
		''' Get the server information

		command: !server_info

		**Usage**:
			`server_info`: Get information about the discord server
		'''
		try:
			embed = discord.Embed()
			embed.set_thumbnail(url=self.bot.user.avatar_url)
			embed.add_field(name='Server created at',
							value=ctx.guild.created_at, inline=False)
			embed.add_field(name='Server Owner', value=ctx.guild.owner.name, inline=False)
			embed.add_field(name='Server ID', value=ctx.guild.id, inline=False)
			embed.add_field(name='Server Name', value=ctx.guild.name, inline=False)
			embed.add_field(name='Total Member', value=f'{ctx.guild.member_count} members')
			embed.add_field(name='Bot Presense', value=f'{len(self.bot.guilds)} Servers')
			embed.set_thumbnail(url=self.bot.user.avatar_url)
			embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
			embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))
	

	@commands.command(name='member_info', help='Get information about the discord member')
	async def member_info(self, ctx, *, member: discord.Member):
		''' Tells you some info about the member

		command: !info_member <member_name>

		**Usage**:
			`member_info`: Get information about the discord member
		'''
		embed = discord.Embed(title=f'{member}', description=f'Here is some info about {member}', color=0x00ff00)
		embed.set_thumbnail(url=self.bot.user.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name='Nickname', value=member.nick, inline=True)
		embed.add_field(name='Status', value=member.status, inline=True)
		embed.add_field(name='Joined at', value=member.joined_at, inline=True)
		embed.add_field(name='Roles', value=len(member.roles), inline=True)
		embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
		embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
		await ctx.send(embed=embed)


	@commands.command(aliases=['bot_info', 'bot_stats'], help='Get information about the bot')
	async def info_bot(self, ctx):
		''' Get information about the bot

		command: !bot_info

		**Usage**:
			`bot_info`: Get information about the bot
		'''
		embed = discord.Embed(title='Bot Information', description='Bot Information', color=discord.Color.blue())
		embed.set_thumbnail(url=self.bot.user.avatar_url)
		embed.add_field(name='Bot Name', value='Cybel', inline=False)
		embed.add_field(name='Bot Version', value=bot_version, inline=False)
		embed.add_field(name='Bot Author', value='CodePerfectPlus', inline=False)
		embed.add_field(name='Bot Invite', value='https://top.gg/bot/832137823309004800/invite', inline=False)
		embed.add_field(name='Bot Support Server', value='https://discord.gg/5JxjZB', inline=False)
		embed.add_field(name='Bot Source Code', value='https://github.com/codePerfectPlus/cybel', inline=False)
		embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
		embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
		await ctx.send(embed=embed)


	@commands.command(aliases=['member_count_server'], help='Get the member count of the server')
	async def member_count(self, ctx): # REVIEW: add online/offline status
		''' Get the member count of the server '''
		embed = discord.Embed(title='Server Status', color=discord.Color.blue())
		embed.set_thumbnail(url=self.bot.user.avatar_url)
		embed.add_field(name='Member Count', value=ctx.guild.member_count, inline=False)
		embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
		embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
		await ctx.send(embed=embed)


	@commands.command(aliases=['get_avatar_user'], help='get the avatar of the user')
	async def get_avatar(self, ctx, member: discord.Member = None):
		''' Get the avatar of the user

		command: !avatar @user

		**Usage**:
			`avatar`: Get the avatar of the user
		'''
		try:
			if member is None:
				member = ctx.author
			embed = discord.Embed(title='Avatar', color=discord.Color.blue())
			embed.set_image(url=member.avatar_url)
			embed.add_field(name='Avatar URL', value=member.avatar_url, inline=False)
			embed.set_thumbnail(url=self.bot.user.avatar_url)
			embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
			embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
			await ctx.send(embed=embed)

		except Exception as e:
			await ctx.send('**`ERROR:`** {} - {}'.format(type(e).__name__, e))


	@commands.command(aliases=['bot_version', 'v', 'version', 'bot_ver'], help='Get the version of the bot')
	async def version_bot(self, ctx):
		''' Get the version of the bot

		command: !bot_version

		**Usage**:
			`bot_version`: Get the version of the bot
		'''
		embed = discord.Embed(title='Bot Version', description=bot_version, color=discord.Color.blue())
		embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
		embed.set_thumbnail(url=self.bot.user.avatar_url)
		embed.set_footer(text='Sponsor by  {}'.format(sponsors['name']), icon_url=sponsors['icon'])
		await ctx.send(embed=embed)


def setup(bot: commands.Bot):
	bot.add_cog(UtilityCommands(bot))