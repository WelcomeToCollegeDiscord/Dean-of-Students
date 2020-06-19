from client import client
import discord

cmd_name = "talk"


@client.command(trigger=cmd_name,
                aliases=["say"])  # aliases is a list of strs of other triggers for the command
async def command(command: str, message: discord.Message):
    a1 = command.split(" ", 2)
    ch_idstr = a1[1]
    text = a1[2]
    role = discord.utils.find(lambda r: r.name == 'Staff', client.message.server.roles)
    daddyid = int(ch_idstr)

    channel = client.get_channel(daddyid)

    if channel is not None and role is not None:
        await channel.send(text)
    else:
        raise TypeError("Invalid or non-existant channel ID (Not a text channel? Vars are", daddyid, text)
