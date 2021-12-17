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

import random

class FunCommands(commands.Cog, name="Fun Commands for Users : Fun Commands"):
	""" Fun Commands 
	
	commands:
		- slot - play a slot machine
		- reverse - reverse a string
		- flip - flip a coin
		- roll - roll a dice
	"""

	def __init__(self, bot):
		self.bot = bot
	
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

	@commands.command(aliases=["flip", "flipcoin", "coinflip"], help="Flip a coin")
	async def flip_the_coin(self, ctx):
		""" Flip the coin randomly

		command: !flipcoin

		**Usage**:
			`flipcoin`: Flip the coin randomly
		"""
		coinsides = ["Heads", "Tails"]
		await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

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


def setup(bot: commands.Bot):
	bot.add_cog(FunCommands(bot))