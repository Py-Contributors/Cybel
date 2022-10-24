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

from src.utils.utils import create_embed


class AdminCommands(commands.Cog, name="Commands for Server Management: Admin Commands"):
    """ Admin Level Commands

    Some commands May Require administrator access.

    Commands:
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
        change_bot_username - Change the username of bot
        change_bot_avatar - Change the avatar of bot
        change_bot_game - Change the game of bot
        change_nickname - Change the nickname of a user.

    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="create category in server")
    @commands.has_permissions(administrator=True)
    async def create_category(self, ctx, category: str):
        """ Command for create category in Guild/Server.

        command: !create_category <category_name>

        **Usage**:
            create category in guild/server.
            Cybel Need administrator access for create category.
        """
        await ctx.guild.create_category(category)
        embed = create_embed(ctx, title="New Category Created", color=discord.Color.blue())
        embed.add_field(name="Created Category", value=category)
        embed.add_field(name="Created by", value=ctx.author.mention)
        await ctx.send(embed=embed)

    @commands.command(help="delete category in server")
    @commands.has_permissions(administrator=True)
    async def delete_category(self, ctx, category: discord.CategoryChannel):
        """ Command for delete category from server

        command: !delete_category <category_name>

        **Usage**:
            delete category from server.
            Cybel Need administrator access for delete category.
        """
        await category.delete()
        embed = create_embed(ctx, title="Category Deleted", color=discord.Color.blue())
        embed.add_field(name="Deleted Category", value=category)
        embed.add_field(name="Deleted by", value=ctx.author.mention)
        await ctx.send(embed=embed)

    @commands.command(help="create text channel in server")
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
        embed = create_embed(ctx, description=f'{channel} got created by {ctx.author.mention}', color=discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.command(help="delete text channel in server")
    @commands.has_permissions(administrator=True)
    async def delete_text_channel(self, ctx, channel: discord.TextChannel):
        """ Command for delete text channel

        command: !delete_text_channel <channel_name>

        **Usage**:
            delete text channel from server.
            Cybel Need administrator access for delete text channel.
        """
        await channel.delete()
        embed = create_embed(ctx, title="Text Channel Deleted", color=discord.Color.blue())
        embed.add_field(name="Deleted Text Channel", value=channel)
        embed.add_field(name="Deleted By", value=ctx.author.mention)
        await ctx.send(embed=embed)

    @commands.command(help="create voice channel in server")
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

    @commands.command(help="delete voice channel in server")
    @commands.has_permissions(administrator=True)
    async def delete_voice_channel(self, ctx, channel: discord.VoiceChannel):
        """ Command for delete voice channel

        command: !delete_voice_channel <channel_name>

        **Usage**:
            delete voice channel from server.
            Cybel Need administrator access for delete voice channel.
        """
        await channel.delete()
        embed = create_embed(ctx, title="Voice Channel Deleted", color=discord.Color.blue())
        embed.add_field(name="Deleted Voice Channel", value=channel)
        embed.add_field(name="Deleted By", value=ctx.author.mention)
        await ctx.send(embed=embed)

    @commands.command(help="create a role in server")
    @commands.has_permissions(manage_roles=True)
    async def create_role(self, ctx, *, new_role_name):
        """ Create New Roles in the Server

        command: !create_role <role_name>

        **Usage**:
            create new role in server.
            Cybel Need manage_roles permission for create new role.
        """
        await ctx.guild.create_role(name=new_role_name)
        embed = create_embed(ctx, title="New Role Created", color=discord.Color.blue())
        embed.add_field(name="Role", value=new_role_name)
        embed.add_field(name="Approved by", value=ctx.author.mention)
        await ctx.send(embed=embed)

    @commands.command(help="delete a role in server")
    @commands.has_permissions(manage_roles=True)
    async def delete_role(self, ctx, role: discord.Role):
        """ Command for delete role

        command: !delete_role <role_name>

        **Usage**:
            delete role from server.
            Cybel Need manage_roles permission for delete role.
        """
        await role.delete()
        embed = create_embed(ctx, title="Role Deleted", color=discord.Color.blue())
        embed.add_field(name="Deleted Role", value=role)
        embed.add_field(name="Deleted by", value=ctx.author.mention)
        await ctx.send(embed=embed)

    @commands.command(aliases=["assign_role"], help="assign role to user")
    @commands.has_permissions(manage_roles=True)
    async def give_role(self, ctx, member: discord.Member, role: discord.Role):
        """ Give role to Server's members

        command: !give_role <member_name> <role_name>

        **Usage**:
            give role to server's members.
            Cybel Need manage_roles permission for give role.
        """
        await member.add_roles(role)
        embed = create_embed(ctx, title="New Role Assigned", color=discord.Color.blue())
        embed.add_field(name="Member", value=member.mention)
        embed.add_field(name="New Role", value=role.name)
        embed.add_field(name="Assigned by", value=ctx.author.mention)
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

    @commands.command(help="send message to user dm")
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
        except Exception:
            await ctx.send(f"{member.mention} have DMs disabled")

    @commands.command(aliases=["chnick"], help="change the user's nickname")
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


async def setup(bot: commands.Cog):
    await bot.add_cog(AdminCommands(bot))
