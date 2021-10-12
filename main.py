import discord
#import os
import json
import requests
import random

client = discord.Client()


sad = ['sad', 'depression', 'depressed', 'misery', 'miserable', 'dukh', 'angry', 'anger', 'dukhi', 'gussa', 'gnda', 'dard', 'pain', 'unhappy']
sad_reply = ["Whenever you need to call, I'm here.",
"I wish I could be there right now.",
"You're still in my thoughts. Remember that.",
"Hey, I haven’t forgotten about you or how difficult this must be. You’re showing a lot of strength.",
"Shit happens to everyone. Not everyone deals with it as well as you."]

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
    if any(word in message.content for word in sad):
        await message.channel.send(random.choice(sad_reply))


client.run('ODk2ODEyNjQ3NDEwOTc0NzYw.YWMj3Q.WQj39Xxqh5WJs1jgDkmfG9XbfsQ')