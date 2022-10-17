"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://top.gg/bot/832137823309004800/invite
"""
from discord.ext import commands


class MusicCommands(commands.Cog, name="Commands for music activity."):
    ''' Music Commands

    Args:
        bot (discord.Client): The bot instance.
    
    Methods:
        play (discord.ext.commands.command): Plays a song.
        pause (discord.ext.commands.command): Pauses the song.
        resume (discord.ext.commands.command): Resumes the song.
        skip (discord.ext.commands.command): Skips the song.
        queue (discord.ext.commands.command): Shows the queue.
        clear (discord.ext.commands.command): Clears the queue.
        volume (discord.ext.commands.command): Changes the volume.
        leave (discord.ext.commands.command): Leaves the voice channel.
        join (discord.ext.commands.command): Joins the voice channel.
        play_next (discord.ext.commands.command): Plays the next song.
        play_prev (discord.ext.commands.command): Plays the previous song.
        play_random (discord.ext.commands.command): Plays a random song.
        play_loop (discord.ext.commands.command): Plays a looped song.
        play_shuffle (discord.ext.commands.command): Plays a shuffled song.
        play_repeat (discord.ext.commands.command): Plays a repeated song.
        play_repeat_one (discord.ext.commands.command): Plays a repeated song.
        play_shuffle_one (discord.ext.commands.command): Plays a shuffled song.
        play_shuffle_all (discord.ext.commands.command): Plays a shuffled song.
        
    '''
    def __init__(self, bot):
        ''' Initializing the cog and passing the bot instance. '''
        self.bot = bot

        
async def setup(bot: commands.Cog):
    await bot.add_cog(MusicCommands(bot))
