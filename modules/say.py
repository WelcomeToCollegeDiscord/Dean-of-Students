from client import client
import discord

cmd_name = "talk"


@client.command(trigger=cmd_name,
                aliases=["say"])  # aliases is a list of strs of other triggers for the command
async def command(command: str, msg: discord.Message):
    ch_id, text = command.split(" ", 1)
    chg = 195582200270290944
    channel = client.get_channel(ch_id)
    if channel is not None and msg.author.id(195582200270290944):
        await channel.send(text)
    else:
        await msg.chg.send("The CHID was", ch_id, "and the text was", text)
    raise TypeError("Invalid or non-existant channel ID (Not a text channel?)")