"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
"""

import random
from discord.ext import commands
import discord
import random
import datetime

from src.utils.utils import bot_version
from src.utils.help import DBHelper

class OtherCommands(commands.Cog, name="Useful Commands for Users : Other Commands"):
	"""
		Other Commands: Other discord server commands

	Commands:

		- bot_version - Get the version of the bot
		- server_invite - Create an invite link for the bot
		- bot_invite - Get the invite link of the bot
		- member_info - Get information about the discord member
		- server_info - Get information about the discord server
		- bot_info - Get information about the bot
		- roll_the_dice - Roll the dice (1-6)
		- flip_the_coin - Flip the coin (heads/tails)
		- report - Report a user to the server owner for misconduct
		- member_count - Get the member count of the server (online/offline)
		- avatar - Get the avatar of the user
		- server_icon - Get the server icon
		- server_id - Get the server id
		- server_name - Get the server name
		- server_owner - Get the server owner
		- reverse - Reverse the text
		- slot - Play the slot machine
		- source - Get the source code of the bot

	"""
	def __init__(self, bot):
		self.bot = bot
		self.db = DBHelper()

	@commands.command(aliases=["test", "hi", "hello", "pong"], help="Get the ping of the bot")
	async def ping(self, ctx):
		"""
			Get the ping of the bot

		command: !ping

		**Usage**
			get the latency of the bot
		"""
		embed = discord.Embed(title="Pong 🏓", description=f"{round(self.bot.latency * 1000)}ms")
		await ctx.send(embed=embed)


	@commands.command(aliases=['bot_version', "version", "bot_ver"], help="Get the version of the bot")
	async def version_bot(self, ctx):
		""" Get the version of the bot
		
		command: !bot_version

		**Usage**:
			`bot_version`: Get the version of the bot
		"""
		await ctx.send(embed=discord.Embed(title="Bot Version", description=bot_version))


	@commands.command(aliases=["server_link"], help="Create an invite link for the server")
	async def server_invite(self, ctx):
		""" Create instant invite for Channel

		command: !create_invite

		**Usage**:
			`server_invite`: Create an invite link for the bot
		
		"""
		link = await ctx.channel.create_invite(unique=False)
		await ctx.send(embed=discord.Embed(title="Server Invite Link", description=link))


	@commands.command(aliases=["bot_invite", "bot_link"], help="Get the invite link of the bot")
	async def invite_bot(self, ctx):
		""" Get invite link for bot

		command: !bot_invite

		**Usage**:
			`bot_invite`: Get the invite link of the bot
		"""
		# FIXME: generate bot invite dynamically
		link = "https://top.gg/bot/832137823309004800/invite"
		await ctx.send(embed=discord.Embed(title="Bot Invite Link", description=link))


	@commands.command(name="member_info", help="Get information about the discord member")
	async def member_info(self, ctx, *, member: discord.Member):
		""" Tells you some info about the member 
		
		command: !info_member <member_name>

		**Usage**:
			`member_info`: Get information about the discord member
		"""
		embed = discord.Embed(title=f"{member}", description=f"Here is some info about {member}", color=0x00ff00)
		embed.set_thumbnail(url=member.avatar_url)
		embed.add_field(name="Nickname", value=member.nick, inline=True)
		embed.add_field(name="Status", value=member.status, inline=True)
		embed.add_field(name="Joined at", value=member.joined_at, inline=True)
		embed.add_field(name="Roles", value=len(member.roles), inline=True)
		embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)


	@commands.command(name="server_info", help="Get information about the discord server")
	async def server_info(self, ctx):
		""" Get the server information

		command: !server_info
		
		**Usage**:
			`server_info`: Get information about the discord server
		"""
		try:
			embed = discord.Embed(title=ctx.guild.name,
								  timestamp=datetime.datetime.utcnow(),
								  color=discord.Color.blue())
			embed.add_field(name="Server created at",
							value=ctx.guild.created_at, inline=False)
			embed.add_field(name="Server Owner", value=ctx.guild.owner.name, inline=False)
			embed.add_field(name="Server ID", value=ctx.guild.id, inline=False)
			embed.add_field(name="Total Member", value=f"{ctx.guild.member_count} members")
			embed.add_field(name="Bot Presense", value=f"{len(self.bot.guilds)} Servers")
			embed.set_thumbnail(
				url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
			embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command(aliases=["bot_info", "bot_stats"], help="Get information about the bot")
	async def info_bot(self, ctx):
		""" Get information about the bot

		command: !bot_info
		
		**Usage**:
			`bot_info`: Get information about the bot
		"""
		embed = discord.Embed(title="Bot Information", description="Bot Information", color=discord.Color.blue())
		embed.add_field(name="Bot Name", value="Cybel", inline=False)
		embed.add_field(name="Bot Version", value=bot_version, inline=False)
		embed.add_field(name="Bot Author", value="CodePerfectPlus", inline=False)
		embed.add_field(name="Bot Invite", value="https://top.gg/bot/832137823309004800/invite", inline=False)
		embed.add_field(name="Bot Support Server", value="https://discord.gg/5JxjZB", inline=False)
		embed.add_field(name="Bot Source Code", value="https://github.com/codePerfectPlus/cybel", inline=False)
		embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)


	@commands.command(aliases=["dice", "roll"], help="Roll a dice")
	async def roll_the_dice(self, ctx, dice: str):
		"""Rolls a dice in NdN format.

		command: !dice NdN

		**Usage**:
			`dice`: Roll a dice in NdN format
		
		number of rolls-d-number of limit

		input: 6d5
		output example: 2, 1, 4, 3, 5
		"""
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			return 'Format has to be in NdN!'

		result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		embed = discord.Embed(title="Dice Rolled", description=f"{ctx.author.mention} rolled dice(1 -{limit}) {rolls} times", color=0x00ff00)
		embed.add_field(name="Result", value=result, inline=False)
		embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)


	@commands.command(aliases=["flip", "flipcoin", "coinflip"], help="Flip a coin")
	async def flip_the_coin(self, ctx):
		""" Flip the coin randomly

		command: !flipcoin
		
		**Usage**:
			`flipcoin`: Flip the coin randomly
		"""
		coinsides = ["Heads", "Tails"]
		await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")


	@commands.command(aliases=["report_user"], help="Report a user")
	async def report(self, ctx, reported_member:discord.Member, *reason):
		""" Report a user

		command: !report @user reason
		
		**Usage**:
			`report`: Report user for misbehavior, abuse, suspicious behaviour etc.
		"""
		try:
			reason = ' '.join(reason)
			embed = discord.Embed(title="Report Status", color=discord.Color.red())
			embed.add_field(name="Reported User", value=reported_member.mention, inline=False)
			embed.add_field(name="Reported By", value=ctx.author.mention)
			embed.add_field(name="Reported to", value=ctx.guild.owner.mention)
			embed.add_field(name="Reason", value=reason, inline=False)
			embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)

			self.db.create_report(datetime.datetime.utcnow().timestamp(),
				ctx.guild.id, reported_member.id, ctx.author.id, ctx.guild.owner.id, reason)
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')

    # REVIEW: add online/offline status
	@commands.command(aliases=["member_count_server"], help="Get the member count of the server")
	async def member_count(self, ctx):
		""" Get the member count of the server """
		embed = discord.Embed(title="Server Status", color=discord.Color.blue())
		embed.add_field(name="Member Count", value=ctx.guild.member_count, inline=False)
		embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)


	@commands.command(aliases=["get_avatar_user"], help="get the avatar of the user")
	async def get_avatar(self, ctx, member: discord.Member = None):
		""" Get the avatar of the user

		command: !avatar @user
		
		**Usage**:
			`avatar`: Get the avatar of the user
		"""
		try:
			if member is None:
				member = ctx.author
			embed = discord.Embed(title="Avatar", color=discord.Color.blue())
			embed.set_image(url=member.avatar_url)
			embed.add_field(name="Avatar URL", value=member.avatar_url, inline=False)
			embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
			
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command(aliases=["icon"], help="get the server icon")
	async def server_icon(self, ctx):
		""" Get the server icon

		command: !server_icon
		
		**Usage**:
			`server_icon`: Get the server icon
		"""
		try:
			embed = discord.Embed(title="Server Icon", color=discord.Color.blue())
			embed.set_image(url=ctx.guild.icon_url)
			embed.add_field(name="Server Icon URL", value=ctx.guild.icon_url, inline=False)
			embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')
	

	@commands.command(help="get the server name")
	async def server_name(self, ctx):
		""" Get the server name

		command: !server_name
		
		**Usage**:
			`server_name`: Get the server name
		"""
		try:
			embed = discord.Embed(title="Server Information", color=discord.Color.blue())
			embed.add_field(name="Server Name", value=ctx.guild.name, inline=False)
			embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')
		

	@commands.command(help="get the server owner")
	async def server_owner(self, ctx):
		""" Get the server owner

		command: !server_owner
		
		**Usage**:
			`server_owner`: Get the server owner
		"""
		try:
			embed = discord.Embed(title="Server Information", color=discord.Color.blue())
			embed.add_field(name="Server Owner", value=ctx.guild.owner.mention, inline=False)
			embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')


	@commands.command(help="get the server id")
	async def server_id(self, ctx):
		""" Get the server id

		command: !server_id
		
		**Usage**:
			`server_id`: Get the server id
		"""
		try:
			embed = discord.Embed(title="Server Information", color=discord.Color.blue())
			embed.add_field(name="Server ID", value=ctx.guild.id, inline=False)
			embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')
	

	@commands.command(help="reverse the text")
	async def reverse(self, ctx, *, text: discord.Message):
		""" Reverse the text

		command: !reverse <text>
		
		**Usage**:
			`reverse`: Reverse the text
		"""
		try:
			await ctx.send(text[::-1])
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')
	

	@commands.command(aliases=["slots", "bet"], help="play slots")
	@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
	async def slot(self, ctx):
		""" Play a slot machine

		command: !slot
		
		**Usage**:
			`slot`: Play a slot machine
		"""
		emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)

		embed = discord.Embed(title="Slot Machine", color=discord.Color.blue())
		embed.add_field(name="**Result**", value=f"{a} {b} {c}", inline=False)
		embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
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
			await ctx.send(f"The bot is powered by **Cybel**\n\n**Source Code**: {source_url}\n\nDon't forget to star the repo if you like it!")
		except Exception as e:
			await ctx.send(f'```{type(e).__name__} - {e}```')
		

def setup(bot: commands.Cog):
	bot.add_cog(OtherCommands(bot))
