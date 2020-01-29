from client import client
import discord


@client.command(trigger="say", aliases=[])
async def say(command: str, message: discord.Message):
    ch_id, text = command.split("", 1)

    channel = client.get_channel(ch_id)
    if channel is not None and message.author.id(195582200270290944):
        await channel.send(text)
        await client.send_message(195582200270290944, "You sent" + text + "to" + ch_id)
    else:
        raise TypeError("Invalid or non-existant channel ID (Not a text channel?)")
