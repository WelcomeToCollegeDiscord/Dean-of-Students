from datetime import datetime
from client import client
import discord


@client.member_join
async def join_notification(member: discord.Member):
    if "discord.gg" in member.name and member.guild.id == 662417141080916001:
        try:
            await member.ban()
        except:
            await client.get_channel(663209067900174336).send(
                "Attempted to autoban user below for \"discord.gg\" in username but failed!")
        else:
            await client.get_channel(663209067900174336).send(
                "Successfully autobanned below user for \"discord.gg\" in username.")
    if member.guild.id == 662417141080916001:
        with open("logs/members.log", "a") as lf:
            lf.write(f"{member.joined_at.__str__()}+{member.guild.member_count - 13}\n")
        embed = discord.Embed(title="Member has joined the server", description=discord.Embed.Empty, colour=0x15a216)
        embed = embed.set_thumbnail(url=member.avatar_url_as(static_format="png", size=1024))
        embed = embed.add_field(name="Tag", value=f"{member.name}#{member.discriminator}")
        embed = embed.add_field(name="ID", value=member.id)
        embed = embed.add_field(name="Mention", value=member.mention)
        embed = embed.add_field(name="New Member Count", value=member.guild.member_count - 13)
        created_ts = (await client.fetch_user(member.id)).created_at
        embed = embed.add_field(name="Account Created At",
                                value=f"{created_ts.__str__()}\n{str(datetime.utcnow() - created_ts)}")
        embed = embed.set_footer(text=member.joined_at)
        await client.get_channel(663209067900174336).send(embed=embed)


@client.member_remove
async def leave_notification(member: discord.Member):
    if member.guild.id == 662417141080916001:
        with open("logs/members.log", "a") as lf:
            lf.write(f"{datetime.utcnow().__str__()}-{member.guild.member_count - 13}\n")
        now = datetime.utcnow()
        embed = discord.Embed(title="Member has left the server", description=discord.Embed.Empty, colour=0xcd5312)
        embed = embed.set_thumbnail(url=member.avatar_url_as(static_format="png", size=1024))
        embed = embed.add_field(name="Tag", value=f"{member.name}#{member.discriminator}")
        embed = embed.add_field(name="ID", value=member.id)
        embed = embed.add_field(name="Nickname", value=member.display_name)
        embed = embed.add_field(name="Mention", value=member.mention)
        embed = embed.add_field(name="New Member Count", value=member.guild.member_count - 13)
        embed = embed.add_field(name="Member since",
                                value=f"{member.joined_at.__str__()} UTC ({now - member.joined_at})")
        embed = embed.set_footer(text=str(now))
        await client.get_channel(663209067900174336).send(embed=embed)
