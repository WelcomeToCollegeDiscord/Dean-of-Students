from client import client

import discord

cmd_name = "weather"

client.basic_help(title=cmd_name, desc="Pulls up the weather")

detailed_help = {
    "Usage": f"{client.default_prefix}{cmd_name}",
    "Arguments": "F/C and location",
    "Description": "Gets weather from locations.",
    # NO Aliases field, this will be added automatically!
}
client.long_help(cmd=cmd_name, mapping=detailed_help)


@client.command(trigger=cmd_name,
                aliases=["wa"])  # aliases is a list of strs of other triggers for the command
async def command(command: str, message: discord.Message):
    ##TBA

    return
