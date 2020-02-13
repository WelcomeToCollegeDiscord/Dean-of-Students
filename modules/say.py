from client import client
import discord

cmd_name = "talk"


@client.command(trigger=cmd_name,
                aliases=["say"])  # aliases is a list of strs of other triggers for the command
async def command(command: str, msg: discord.Message):
    ch_id, text = command.split(" ", 1)
    channel = client.get_channel(ch_id)
    oof = client.get_channel(663214410667655238)

    if channel is not None:
        await oof.send("Vars are", ch_id. text)
        await channel.send(text)
    else:
        raise TypeError("Invalid or non-existant channel ID (Not a text channel? Vars are", ch_id, text)
