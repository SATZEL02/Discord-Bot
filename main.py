import discord
import os
import json
import requests
import random
import giphy_client
from giphy_client.rest import ApiException
from discord.ext import commands
import aiohttp
import sys
import traceback
from dotenv import load_dotenv
load_dotenv()



client = discord.Client(case_insensitive=True)



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
    #return function
    if message.author == client.user:
        return

    #test function
    if message.content.startswith("!test"):
        await message.channel.send("Bot is working!!")

    #quote function
    if message.content.startswith("!quote"):
        quote = qoute()
        await message.channel.send(quote)

    #motivation function
    if any(word in message.content for word in sad):
        await message.channel.send(random.choice(sad_reply))

    #gif function
    if message.content.startswith('!gif'):
        q = 'Smile'
        api_key=os.getenv('api_key')
        api_instance = giphy_client.DefaultApi()
        Token =  message.content.split(" ")
        if (len(Token) > 1):
            s= ' '

            q = s.join(Token[1:])
        try: 
            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)
            emb = discord.Embed(title=q)
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
            await message.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    #meme function
    if message.content.startswith('!meme'):
        # q = 'memes'
        # meme_key =  message.content.split(" ")
        # if (len(meme_key) > 1):
        #     a= ' '

        #     q = a.join(meme_key[1:])
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/memes.json") as r:
                memes = await r.json()
                embed = discord.Embed(color = discord.Color.purple())
                embed.set_image(url=memes['data']['children'] [random.randint(0, 25)]['data']['url'])
                embed.set_footer(text = f"Meme requested by {message.author}")
                await message.channel.send(embed=embed)




client.run(os.getenv('TOKEN'))
