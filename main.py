import discord
import os
import json
from discord.channel import VoiceChannel
import requests
import random
import giphy_client
from giphy_client.rest import ApiException
from discord.ext import commands
import sys
import traceback



# client = commands.Bot(command_prefix = '!')
bot = commands.Bot(command_prefix = '!' , case_insensitive = True)
bot.remove_command('help')


# sad = ['sad', 'depression', 'depressed', 'misery', 'miserable', 'dukh', 'angry', 'anger', 'dukhi', 'gussa', 'gnda', 'dard', 'pain', 'unhappy']
# sad_reply = ["Whenever you need to call, I'm here.",
# "I wish I could be there right now.",
# "You're still in my thoughts. Remember that.",
# "Hey, I haven’t forgotten about you or how difficult this must be. You’re showing a lot of strength.",
# "Shit happens to everyone. Not everyone deals with it as well as you."]

# @client.event
# async def on_ready():
#     print("Hi , I am {0.user}".format(client))
# def qoute():
#     reply = requests.get("https://zenquotes.io/api/random")
#     json_data = json.loads(reply.text)
#     quote = json_data[0]['q'] + " -" + json_data[0]['a']
#     return(quote)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith("!test"):
#         await message.channel.send("Bot is working!!")
#     if message.content.startswith("!quote"):
#         quote = qoute()
#         await message.channel.send(quote)
#     if any(word in message.content for word in sad):
#         await message.channel.send(random.choice(sad_reply))

# @client.event
# async def gif(ctx,*,q = 'Smile'):
#     api_key = 'DEORFvNt9LsDlaMWqAdbHRf8Tj5VbAGu'
#     api_instance = giphy_client.DefaultApi()

# @commands.command()
# async def play(message , ctx , url : str):
#     if message.content.startswith('!join'):
#         VoiceChannel = discord.utils.get(ctx.guild.voice_channels ,name = 'Kithe aa')
#         voice = discord.utils.get(client.voice_client , guild = ctx.guild)
#         await VoiceChannel.connect()

# @client.command(pass_context=True)
# async def join(ctx):
#     channel = ctx.message.author.voice.voice_channel
#     await client.join_voice_channel(channel)
    
@bot.event
async def on_ready():
    print('Lets go!!')

extensions = ['cogs.meme']
if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Error loading {extension}' , file = sys.stderr)
            traceback.print_exc()


bot.run('ODk2ODEyNjQ3NDEwOTc0NzYw.YWMj3Q.WQj39Xxqh5WJs1jgDkmfG9XbfsQ')