import asyncio
import sys
import traceback 
from discord.ext import commands
import discord
from discord import PartialEmoji, app_commands
from typing import Any, Optional, Union
from discord.emoji import Emoji
from discord.enums import ButtonStyle
from discord.ext import commands
from discord.interactions import Interaction


seconds = 0

class RuneTimerButton(discord.ui.Button):
    def __init__(self, style, label, mode, time: int, bot):
        super().__init__(style=style, label=label)
        self.mode = mode
        self.bot = bot
        self.time = time

    #onclick button 
    async def callback(self, interaction: Interaction):
        await interaction.response.defer()
        voice_channel = interaction.user.voice.channel
        voice_client_list = self.bot.voice_clients

        if not voice_client_list:
            voice_client = await voice_channel.connect()
        else:
            print("durch move gejoined")
            voice_client = await self.bot.voice_clients[0].move_to(voice_channel)
        
        voice_client = self.bot.voice_clients[0]

        print(voice_client)
        #start
        #DASIMMERMAMMAAAA
        if self.mode == 0:
            #asyncio.create_task(InteractionHandler.RuneTimer(self, self.time))
            global seconds 
            seconds = 3
            meinHandler = InteractionHandler(self.bot)
            await meinHandler.RuneTimer(self, voice_client, self.time)

            #voice_client.play(discord.FFmpegPCMAudio(source=".\\voicelines\\gogogo.wav", executable=".\\cogs\\ffmpeg.exe"))
        #stop
        elif self.mode == 1:
            voice_client.stop()
            #interaction.client.voice_clients[0].play(discord.FFmpegPCMAudio(source=".\\voicelines\\bye.mp3", executable=".\\cogs\\ffmpeg.exe"))
            await voice_client.disconnect()




class RuneTimerView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.add_item(RuneTimerButton(ButtonStyle.success, "Start", 0, 0, bot))
        #117 seconds for strat
        self.add_item(RuneTimerButton(ButtonStyle.secondary, "Strat 10", 0, 2, bot))
        self.add_item(RuneTimerButton(ButtonStyle.secondary, "In 60", 0, 60, bot))
        self.add_item(RuneTimerButton(ButtonStyle.red, "Stop", 1, -1, bot))


class Timer():
    def __init__(self, bot):
        self.bot = bot


class InteractionHandler(commands.Cog):   
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="runes")
    async def runetimer(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=RuneTimerView(self.bot))
        
    #HIER SIMMER
    async def RuneTimer(self, vc: discord.voice_client, seconds: int):
        await asyncio.sleep(seconds)
        await vc.play(discord.FFmpegPCMAudio(source=".\\voicelines\\gogogo.wav", executable=".\\cogs\\ffmpeg.exe"))

async def setup(bot):
    await bot.add_cog(InteractionHandler(bot))

"""
    @app_commands.command()
    async def deletemessages(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message("noice", ephemeral=True)

    @commands.command(name='connect', aliases=['join'])
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        Connect to voice.
        Parameters
        ------------
        channel: discord.VoiceChannel [Optional]
            The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
            will be made.
        This command also handles moving the bot to different channels.
        
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise InvalidVoiceChannel('No channel to join. Please either specify a valid channel or join one.')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Moving to channel: <{channel}> timed out.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Connecting to channel: <{channel}> timed out.')

        await ctx.send(f'Connected to: **{channel}**', delete_after=20)
"""
