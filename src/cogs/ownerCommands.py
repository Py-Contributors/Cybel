"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:- https://top.gg/bot/832137823309004800/invite
"""

import discord
from discord.ext import commands

from src.utils.dbhelper import DBHelper


class OwnerCommands(commands.Cog, name="Commands for Bot Owner only (Developer)"):
    """ Testing commands """

    def __init__(self, bot):
        self.bot = bot
        self.db = DBHelper()

    @commands.command(help="change the username of bot")  # change bot the
    @commands.is_owner()
    async def change_bot_username(self, ctx, new_username: str):
        """ Change username

        command: !change_bot_username <new_username>

        **Usage**:
            change username of server.
            Cybel Need administrator permission for change username.
        """
        try:
            await ctx.bot.user.edit(username=new_username)
            await ctx.send(f"Username changed to {new_username}")
        except Exception as e:
            await ctx.send(f'```{type(e).__name__} - {e}```')

    @commands.command(help="change the avatar of bot")  # FIXME: change avatar is not working
    @commands.is_owner()
    async def change_bot_avatar(self, ctx, *, new_avatar: str):
        """ Change avatar of bot

        command: !avatar <new_avatar>

        **Usage**:
            change avatar of server.
            Cybel Need administrator permission for change avatar.
        """
        try:  # update bot avatar
            await ctx.bot.user.edit(avatar=new_avatar)
            await ctx.send(f"Avatar changed to {new_avatar}")
        except Exception as e:
            await ctx.send(f'```{type(e).__name__} - {e}```')

    @commands.command(help="change the bot status")
    @commands.is_owner()
    async def change_bot_game(self, ctx, new_game: str):
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

    @commands.command(help="change the bot status")  # REVIEW: have to review this command
    @commands.is_owner()
    async def change_bot_status(self, ctx, new_status: str):
        """ Change status

        command: !status <new_status>

        **Usage**:
            change status of server.
            Cybel Need administrator permission for change status.
        """
        try:
            if new_status == "online":
                await ctx.bot.change_presence(status=discord.Status.online)
            elif new_status == "idle":
                await ctx.bot.change_presence(status=discord.Status.idle)
            elif new_status == "dnd":
                await ctx.bot.change_presence(status=discord.Status.dnd)
            elif new_status == "offline":
                await ctx.bot.change_presence(status=discord.Status.offline)
            else:
                await ctx.send("Invalid status")
            await ctx.send(f"Status changed to {new_status}")
        except Exception as e:
            await ctx.send(f'```{type(e).__name__} - {e}```')

    @commands.command(help="change the bot status")  # REVIEW:- have to review this command
    @commands.is_owner()
    async def change_bot_activity(self, ctx, new_activity: str):
        """ Change activity

        command: !activity <new_activity>

        **Usage**:
            change activity of server.
            Cybel Need administrator permission for change activity.
        """
        try:
            await ctx.bot.change_presence(activity=discord.Activity(name=new_activity))
            await ctx.send(f"Activity changed to {new_activity}")
        except Exception as e:
            await ctx.send(f'```{type(e).__name__} - {e}```')


async def setup(bot: commands.Bot):
    await bot.add_cog(OwnerCommands(bot))
