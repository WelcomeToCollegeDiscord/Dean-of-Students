from client import client
import discord


@client.message()
async def talk(command: str, message: discord.Message):
    ch_id = command[2:]
    text = command[3:]

    channel = client.get_channel(ch_id)
    if channel is not None:
        await channel.send(text)
    else:
        raise TypeError("Invalid or non-existant channel ID (Not a text channel?)")
