from client import client
import discord

cmd_name = "talk"


@client.command(trigger=cmd_name,
                aliases=["say"])  # aliases is a list of strs of other triggers for the command
async def command(command: str, msg: discord.Message):
    a1 = command.split(" ", 2)
    chid = a1[1]
    text = a1[2]

    channel = client.get_channel(chid)

    if channel is not None:  # and message.author.id(195582200270290944):
        await channel.send(text)
    else:
        raise TypeError("Invalid or non-existant channel ID (Not a text channel? Vars are", chid, text)
