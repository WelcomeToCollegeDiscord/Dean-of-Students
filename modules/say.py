from client import client
import discord

cmd_name = "talk"


@client.command(trigger=cmd_name,
                aliases=["say"])  # aliases is a list of strs of other triggers for the command
async def command(command: str, msg: discord.Message):
    gui, ch_id, text = command.split(" ", 3)
    channel = client.get_channel(ch_id)
    guild = client.get_guild(gui)
    if channel is not None:
        await guild.channel.send(text)
    else:
        raise TypeError("Invalid or non-existant channel ID (Not a text channel? Vars are", ch_id, text)
