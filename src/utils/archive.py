
from better.profanity import profanity

async def on_message(self, message):
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