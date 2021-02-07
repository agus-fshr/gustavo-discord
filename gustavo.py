import discord
import re
import urllib.request
import os

client = discord.Client()

mails_list = os.getenv(MAILS)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:
        mail = re.findall('\S+@itba.edu.ar', message.content)
        if mail != []:
            #print(mail)
            mail2 = str(mail)
            mail2 = mail2[2:-2]
            print('Checking ', mail2)
            for buscador in mails_list:
                if mail2==buscador:
                    channel = client.get_channel(os.getenv(CANAL))
                    alerta = str(mail2), '  <---- Este mail es de la blacklist!'
                    await channel.send(alerta)

        else:
            return

###Insert discord API token below
client.run(os.getenv(TOKEN))
