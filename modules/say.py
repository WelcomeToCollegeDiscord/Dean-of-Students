from client import client
import discord


@client.command(trigger="say", aliases=[])
async def talk(command: str, message: discord.Message):
    text, ch_id = command.split(" ", 1)
    channel = client.get_channel(ch_id)
    chid = 663214410667655238
    cchhidd = client.get_channel(chid)
    if channel is not None and message.author.id(195582200270290944):

        await channel.send(text)
    else:
        await cchhidd.send(text, ch_id)
