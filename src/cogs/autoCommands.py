"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot

"""
import discord
from discord.ext import commands
import aiohttp
from src.utils import utils
from src.utils import logging


class AutoCommands(commands.Cog):
    """ These commands will fire automatically."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Activity(type=discord.ActivityType.watching, name="Everyone")
        await self.bot.change_presence(activity=activity)
        logging.info(f'{self.bot.user.name} is Online...')

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = member.guild.system_channel
        if channel is not None:
            welcome_msg = discord.Embed(title="Welcome",
                                        description=f"welcome {member.mention}, Introduce yourself to community.")
            welcome_msg.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
            await channel.send(embed=welcome_msg)
            await member.send("welcome to the Server!\nPlease introduce yourself in server.\nOfficial Server for Cybel https://discord.gg/JfbK3bS")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = member.guild.system_channel
        if channel is not None:
            bye_msg = discord.Embed(title="Good Bye",
                                    description=f"{member} has left the server.")
            bye_msg.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/831943037936467985/835036938326638622/cybel.png")
            await channel.send(embed=bye_msg)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("**Invalid command. Try using** `!help` **to figure out commands!**")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please pass in all requirements.** check `!help <command>` for all requirements')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("**You dont have all the requirements or permissions for using this command :angry:**")

"""
    # TODO - on reaction add
    @commands.Cog.listener()
    async def on_raw_reaction_add(self):
        pass

    # TODO - on Reaction remove
    @commands.command()
    async def on_raw_reaction_remove(self):
        pass
"""

def setup(bot: commands.Cog):
    bot.add_cog(AutoCommands(bot))
