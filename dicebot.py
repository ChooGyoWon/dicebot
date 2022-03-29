import discord
import os
import random

client = discord.Client()

sanchi = ["성공","성공","실패","실패","펌블","성공","실패","성공"]
    

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    # 봇의 단어에는 반응하지 않게

  msg = message.content

  if msg.startswith('!'):
    msg=msg.lstrip('!')
    msgsplit=msg.split('d')
    rollnum=int(msgsplit[0])
    dicenum=int(msgsplit[1])
     
    diceroll = []
    for i in range(0, rollnum):
      diceroll.append(str(random.randrange(0,dicenum)+1))

    diceresult="```"+str(diceroll)+"```"
    await message.channel.send(diceresult)

  if msg.startswith('$산치체크'):
    await message.channel.send(random.choice(sanchi))
    # 봇이 반응할 단어


client.run(os.getenv('TOKEN'))