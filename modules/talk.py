from client import client
import discord


@client.message()
async def talk(command: str, message: discord.Message):
    msg = command[2:]
    oof = command[3:]
    message.get_channel(oof)
    if message.author.id("195582200270290944"):
        try:
            await message.channel.send(msg)
        except:  # that's fine, we don't care
            pass
