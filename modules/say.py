from client import client
import discord


@client.command(trigger="say", aliases=[])
async def talk(command: str, message: discord.Message):
    text, ch_id = command.split(' ', 1)
    channel = client.get_channel(ch_id)

    if channel is not None and message.author.id(195582200270290944):

        await channel.send(text)
    else:
        await message.send_message("195582200270290944", "Nope :( vars are " + ch_id + "and" + text)
