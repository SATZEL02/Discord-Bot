import discord
#import os

client = discord.Client()

@client.event
async def on_ready():
    print("Hi , I am {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("**Test"):
        await message.channel.send("Bot is working!!")
client.run('ODk2ODEyNjQ3NDEwOTc0NzYw.YWMj3Q.WQj39Xxqh5WJs1jgDkmfG9XbfsQ')