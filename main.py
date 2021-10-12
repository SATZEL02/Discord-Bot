import discord
#import os
import json
import requests
client = discord.Client()

@client.event
async def on_ready():
    print("Hi , I am {0.user}".format(client))
def qoute():
    reply = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(reply.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!test"):
        await message.channel.send("Bot is working!!")
    if message.content.startswith("!quote"):
        quote = qoute()
        await message.channel.send(quote)
client.run('ODk2ODEyNjQ3NDEwOTc0NzYw.YWMj3Q.WQj39Xxqh5WJs1jgDkmfG9XbfsQ')