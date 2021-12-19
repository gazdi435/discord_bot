import discord
import os
import random
from keepalive import keep_alive
from replit import db
from discord.ext import commands


Token = os.environ['Token']
NEM = db["aranyk"]
PREFIX = ("%")
players = {}


client = discord.Client()

@client.event
async def on_ready():
  print('A bot be van jelentkezve mint: {0.user}'.format(client))
  activity = discord.Activity(type=discord.ActivityType.watching, name="Téged")
  await client.change_presence(activity=activity)
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content == "%aranyk": #random aranyköpés
    await message.channel.send(random.choice(db["aranyk"]))
  if message.content == "%aranyk all": #összes aranyköpés kiiratása
    for idezet in db["aranyk"]:
      await message.channel.send(idezet)
  if message.content.startswith("%aranyk add"): #aranyköpés hozzáadása
    message.content.split(" ")
    db["aranyk"].append(message.content[12:])
    await message.channel.send("Az idézet sikeresen hozzá lett adva: ")
    await message.channel.send(db["aranyk"][-1])
  if message.content == ("%aranyk del"): #aranyköpés törlése
    db["aranyk"].pop(-1)
    await message.channel.send("Az legutóbb hozzáadott idézet el lett távolítva!")
  if message.content == "%parancsok": #összes parancs
    await message.channel.send("A bot csak a %-el kezdődő parancsokra reagál.\n \n aranyk:\tRandom aranyköpés. \n aranyk add:\tAranyköpés hozzáadása. \n aranyk del:\tLegutóbbi aranyköpés törlése. \n aranyk all:\tAz összes aranyköpés.")
  if message.content.startswith("%aranyk keres"): #Aranyköpés keresés
    for idezet in NEM:
      if message.content[14:] in idezet:
        await message.channel.send(idezet)




keep_alive()
client.run(Token)
