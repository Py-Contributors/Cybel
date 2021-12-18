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

from src.utils import logging
from src.utils.utils import sponsors

class AutoCommands(commands.Cog, name="Auto Commands"):
    """ These commands will fire automatically.
    
    Arguments:
        bot {discord.Cog} -- The bot object.
    
    Commands:
        on_ready -- Fires when the bot is ready.
        on_member_join -- Fires when a member joins the server.
        on_member_remove -- Fires when a member leaves the server.
        on_command_error -- Fires when a command fails.
        on_message_delete -- Fires when a message is deleted.
        on_message_edit -- Fires when a message is edited.
    """

    def __init__(self, bot):
        """ Init function for AutoCommands."""
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        """ This will run when the bot is ready. """
        activity = discord.Activity(type=discord.ActivityType.watching, name="Everyone")
        await self.bot.change_presence(activity=activity)
        logging.info(f'{self.bot.user.name} is Online...')


    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """ This will fire when a new member joins the server."""
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(title="Welcome",
                                        description=f"welcome {member.mention}, Introduce yourself to community.")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
            await channel.send(embed=embed)
            await member.send("welcome to the Server! introduce yourself in server.\nOfficial Server for Cybel help: https://discord.gg/JfbK3bS")


    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """ This event triggers when a member leaves the server."""
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(title="Good Bye",
                                    description=f"{member} has left the server.")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
            await channel.send(embed=embed)
    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """ The event triggered when an error is raised while invoking a command."""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("**Invalid command. Try using** `!help` **to figure out commands!**")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please pass in all requirements.** check `!help <command>` for all requirements')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("**You dont have all the requirements or permissions for using this command :angry:**")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown... try again in {error.retry_after:.2f} seconds.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("**You dont have all the requirements or permissions for using this command :angry:**")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("**An error occurred while executing this command.**")


    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        '''
        on_message_delete event will fire when a message is deleted.

        Arguments:
            message {discord.Message} -- The message object.

        '''
        if message.author.bot:
            return
        elif message.author.id == self.bot.user.id:
            return
        else:
            await message.channel.send(f"**{message.author.mention}**, **Your message has been deleted!**")

    
    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        '''
        on_message_edit event will fire when a message is edited.

        Arguments:
            before {discord.Message} -- The message object before editing.
            after {discord.Message} -- The message object after editing.

        '''
        if before.author.bot:
            return
        elif before.author.id == self.bot.user.id:
            return
        else:
            await after.channel.send(f"**{before.author.mention}**, **Your message has been edited!**")
        
    
def setup(bot: commands.Cog):
    bot.add_cog(AutoCommands(bot))
