from client import client
import discord
import mysql.connector
import key

## All the sql login stuff here
db = mysql.connector.connect(
  host=key.host,
  user=key.dbuser,
  passwd=key.dbpassword,
  database=key.db
  )
 table = 'table';
 
 
 cur = db.cursor()
@client.command(trigger="refreshdb")
async def command(command: str, message: discord.Message):
	members = message.guild.members
	added=0
	for m in members:
		sql = "SELECT EXISTS(SELECT * FROM %s WHERE id = %i)"
		val = ('table',m.id)
		cur.execute(sql,val)
		if(len(cur.fetchall()==0):
			sql = "INSERT INTO %s (id) VALUES (%i)" ## Should be changed to add whatever needs to be input to database
			val = ('table',m.id)
			cur.execute(sql,val)
			added+=1
	return await message.channel.send(("Added",added,"users to database"))
	
	