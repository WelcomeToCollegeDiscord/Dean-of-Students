import log
from client import client
from modules import __common__
from typing import List, Union

import discord

primary_channels: List[int] = [
    662417141080916013,  # general
]

other_channels: List[int] = [
    662458900439891992,  # Intro
    662458453973008385,  # Com Sug
    662569283426975755,  # Animals
    662474366998675521,  # 18+
    662475478946283530,  # Poli
    662638297197314054,  # Dank
    662425705438773248,  # Bot
    662779486294769724,  # College advice
    662779464698036239,  # rate my sec
    662779513855410176,  # homework
    662779589143298068,  # venting
    662421157374328834,  # Anime
    662700520867102721,  # Pics
    662421691095449622,  # sports
    662421823157436432,  # Tech
    662700473756811307,  # travel
    662638434095071242,  # videogame
    662438866501763088,  # VoiceChat
    662439112292433952,  # MusicChat
]

public_voice_channels: List[int] = [
    662417141080916021,  # VC Lounge
    662546485694693397,  # Roundtable
    662439079761281024,  # music

]

lock_help = {
    "Usage": f"`{client.default_prefix}lock`\n"
             f"`{client.default_prefix}unlock`",
    "Arguments": "None",
    "Description": "Locks or unlocks the specified channel in case of a raid or general chaos. This command must be "
                   "run in the target channel. Moderator-only channels cannot be locked. "
}

purge_help = {
    "Usage": f"`{client.default_prefix}purge [n]`",
    "Arguments": "`n` - (Optional) Number of messages to delete, capped at 100. (default 25)",
    "Description": "Nukes some number of recent messages in a channel.",
}
client.long_help("lock", lock_help)
client.long_help("unlock", lock_help)
client.long_help("purge", purge_help)

admin_role = None
if client.is_ready():
    admin_role = client.get_guild(662417141080916001).get_role(664037763863281676)


@client.ready
async def set_mod_role():
    global admin_role
    try:
        admin_role = admin_role = client.get_guild(662417141080916001).get_role(664037763863281676)
    except AttributeError:
        log.critical(f"WTC mod role not found, oof")


@client.command(trigger="lock", aliases=["l"])
async def lock(command: str, message: discord.Message):
    if message.guild.id != 662417141080916001:
        if message.guild.id != 452274699641159683:
            # wrong guild
            await message.channel.send("Invalid server")
            return
    else:
        if admin_role not in message.author.roles:
            # user is not a mod
            await __common__.failure(message)
            return

    parts = command.split(" ")
    # parts = ['lock', arg1]

    # Define it so we can use typing without cluttering it up later
    target: Union[discord.TextChannel, discord.VoiceChannel] = None

    if len(parts) == 1:
        if message.author.voice is not None:
            target = message.author.voice.channel
        else:
            target = message.channel
    else:
        target = message.guild.get_channel(parts[1][2:-1])
    if (target.id not in primary_channels + other_channels + public_voice_channels) and \
            (message.guild.id != 452274699641159683):
        await __common__.failure(message)
        return

    # Take away the proper write/speak permission
    if isinstance(target, discord.TextChannel):
        await target.set_permissions(target=target.guild.default_role,
                                     overwrite=discord.PermissionOverwrite(send_messages=False))
        await message.delete()
        return
    if isinstance(target, discord.VoiceChannel):
        await target.set_permissions(target=target.guild.default_role,
                                     overwrite=discord.PermissionOverwrite(speak=False))
        await message.delete()
        return


@client.command(trigger="unlock", aliases=["ul"])
async def unlock(command: str, message: discord.Message):
    if message.guild.id != 662417141080916001:
        if message.guild.id != 452274699641159683:
            # wrong guild
            await message.channel.send("Invalid server")
            return
    else:
        if admin_role not in message.author.roles:
            # user is not a mod
            await __common__.failure(message)
            return

    parts = command.split(" ")
    # parts = ['unlock', arg1]

    # Define it so we can use typing without cluttering it up later
    target: Union[discord.TextChannel, discord.VoiceChannel] = None

    if len(parts) == 1:
        if message.author.voice is not None:
            target = message.author.voice.channel
        else:
            target = message.channel
    else:
        target = message.guild.get_channel(__common__.strip_to_id(parts[1]))
    if (target.id not in primary_channels + other_channels + public_voice_channels) and \
            (message.guild.id != 452274699641159683):
        await __common__.failure(message)
        return

    # Set the proper write/speak permission
    if isinstance(target, discord.TextChannel):
        await target.set_permissions(target=target.guild.default_role,
                                     overwrite=discord.PermissionOverwrite(send_messages=True))
        await message.delete()
        return
    if isinstance(target, discord.VoiceChannel):
        await target.set_permissions(target=target.guild.default_role,
                                     overwrite=discord.PermissionOverwrite(speak=True))
        await message.delete()
        return


@client.command(trigger="purge", aliases=["nuke"])
async def nuke_old_chat(command: str, message: discord.Message):
    if message.guild.id != 662417141080916001:
        if message.guild.id != 452274699641159683:
            # wrong guild
            await message.channel.send("Invalid server")
            return
    else:
        if admin_role not in message.author.roles:
            # user is not a mod
            await __common__.failure(message)
            return

    parts = command.split(" ")
    if len(parts) == 1:
        count = 25
    else:
        count = int(parts[1])

    target_msgs = await message.channel.history(limit=count).flatten()
    assert isinstance(message.channel, discord.TextChannel)
    assert isinstance(message.guild, discord.Guild)
    await message.channel.delete_messages(target_msgs)
    return


@client.command(trigger="modtools")
async def help_mods(command: str, message: discord.Message):
    embed = discord.Embed(title=f"Tools in {client.bot_name} for moderators",
                          description="Specifically with application to the Young Hams server",
                          colour=0x419bb8)
    embed = embed.add_field(name="Join/Leave Info",
                            value="When a person joins, information about them will be posted such as account name, "
                                  "ID, creation date, and the new member count. When a person leaves, information "
                                  "about them will be posted such as account name, ID, join date, and new member "
                                  "count.")
    embed = embed.add_field(name="Name Autoban",
                            value="Users who attempt to join with `discord.gg` in their name will be autobanned upon "
                                  "joining. This is as a result of the indexing \"virus\" bots that spread around "
                                  "Discord some time ago.")
    embed = embed.add_field(name="Ping Spam Autokick", value="Users who spam too many pings will be automatically "
                                                             "kicked as an anti-spambot/anti-raid measure. Criteria "
                                                             "are either: (A) 30+ pings to a single person within one "
                                                             "minute, or (B) 8+ pings to 8 different people within "
                                                             "one minute.")
    embed = embed.add_field(name="Message and File Logger",
                            value="All messages and files that are sent are automatically saved and downloaded "
                                  "locally (up to 7 days for attachments). This can be used to log users that are "
                                  "banned and inspect suspicious attachments.")
    embed = embed.add_field(name="Channel Locker",
                            value="In case of emergency/chaos, public channels can be locked to calm down chaos. "
                                  "`dean lock` and `dean unlock` can only be run in that target channels, "
                                  "and moderator-only channels cannot be locked/unlocked (attempting to unlock a "
                                  "moderator-only channel would make it publicly accessible).")
    embed = embed.add_field(name="Message Purge",
                            value="When necessary, recent messages in a channel can be purged with `dean purge [n]`, "
                                  "where `n` is the number of messages to delete including the command itself ("
                                  "default 25). Maximum purge size is 100 messages.")
    if admin_role in message.author.roles:
        await message.channel.send(embed=embed)
