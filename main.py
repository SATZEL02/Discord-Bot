import os
import json
import random
import discord
import requests
import giphy_client
from giphy_client.rest import ApiException
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

sad = ['sad', 'depression', 'depressed', 'misery', 'miserable', 'dukh', 'angry', 'anger', 'dukhi', 'gussa', 'gnda', 'dard', 'cry', 'sob', 'crying', 'rona', 'weep','weeping','sobbing', 'pain', 'unhappy'] 
sad_reply = ["Whenever you need to call, I'm here.",
"I wish I could be there right now.",
"You're still in my thoughts. Remember that.",
"Hey, I haven’t forgotten about you or how difficult this must be. You’re showing a lot of strength.",
"Shit happens to everyone. Not everyone deals with it as well as you."]


slang = ['fuck', 'bakchod' , 'baklode' , 'chutiya' , 'behenchod' , 'madarchod' , 'gand' , 'gaand' , 'asshole' , 'chod' , 'chut' , 'loda' , 'choot' , 'lund' , 'lawde' , 'bitch' , 'pancho' , 'behnchod' , 'maachod' , 'bhadwe' , 'bsdk' , 'bhosdike' , 'dick' , 'jhaatu' , 'aulaad' , 'chudwa']
slang_reply = ['A WILD PERSON WITH CALM MIND CAN MAKE ANYTHING , REMEMBER THAT !!', 
'You don’t have to control your thoughts. You just have to stop letting them control you!!',
'Calm your mind life becomes more crystal clear',
'The nearer a man comes to a calm mind the closer he is to strenght' , 
'Mistakes & pressures are inevitable; the secret to getting past them is to stay calm',
'You practice mindfulness, on the one hand, to be calm & peaceful. On the other hand, as you practice mindfulness & live a life of peace, you inspire hope for a future of peace',
'Close your eyes, shut your mind for a while, for there a tranquil land that awaits your presence',
'TAKE A DEEP BREATH!!']


roast_lines = ['You’re the reason God created the middle finger.',
'Your secrets are always safe with me. I never even listen when you tell me them.',
'You bring everyone so much joy when you leave the chat.',
'I’d give you a nasty look but you’ve already got one.',
'Someday you’ll go far. I hope you stay there.',
'Were you born this stupid or did you take lessons?',
'You should really come with a warning label.',
'It’s kind of hilarious watching you try to fit your entire vocabulary into one sentence.',
' I’ll never forget the first time we met. But I’ll keep trying.',
'You are so full of shit, the toilet’s jealous.',
'Stupidity isn’t a crime, so you’re free to go.',
'I love what you’ve done with your hair. How do you get it to come out of the nostrils like that?',
'Too bad you can’t Photoshop your ugly personality.',
'God might love you, but everyone else definitely thinks you’re an idiot.',
"Please just tell me you don’t plan to home-school your kids coz you're stupid af.",
'You see this chat? I want you out of it.',
'If you’re going to act like a turd, go lay on the yard.',
"If you’re going to act like a turd, go lay on the yard.",
'If laughter is the best medicine, your face must be curing the world.',
'Everyone’s entitled to act stupid once in a while, but you really abuse the privilege.',
'Isn’t there a bullet somewhere you could be jumping in front of?',
'If I threw a stick, you’d leave, right?',
'Somewhere out there, there’s a tree working very hard to produce oxygen so that you can breathe. I think you should go and apologize to it.',
'Light travels faster than sound which is why you seemed bright until you spoke.',
'Hold still. I’m trying to imagine you with personality.',
'You are the human version of period cramps.',
'There are some remarkably dumb people in this world. Thanks for helping me understand that.',
'You’ll never be the man your mom is.',
'You are like a cloud. When you disappear it’s a beautiful day.',
'I was hoping for a battle of wits but you appear to be unarmed.',
'I could eat a bowl of alphabet soup and poop out a smarter statement than whatever you just said.',
'People like you are the reason I’m on medication.',
'If you’re going to be two-faced, at least make one of them pretty.',
'Grab a straw, because you suck.',
'Were you born on the highway? That is where most accidents happen.',
'Remember when I asked for your opinion? Me neither.',
'Don’t be ashamed of who you are. That’s your parent’s job.',
'I believed in evolution until I met you.',
'You’re my favorite person… besides every other person I’ve ever met.',
'I envy people who have never met you.',
'People like you are the reason God doesn’t talk to us anymore.',
'Take my lowest priority and put yourself beneath it.',
'You’re impossible to underestimate.']


@client.event
async def on_ready():
    print("Hi , I am {0.user}".format(client))
def qoute():
    reply = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(reply.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']    
    return(quote)

    
# lets begin
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


    #slang function
    if any(word in message.content for word in slang):
        await message.channel.send(random.choice(slang_reply))


    #gif function
    if message.content.startswith('!gif'):
        q = 'Smile'
        api_key=os.getenv('api_key')
        api_instance = giphy_client.DefaultApi()
        Token =  message.content.split(" ")
        if len(Token) > 1:
            s= ' '
            q = s.join(Token[1:])
        try:
            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)
            emb = discord.Embed(title=q)
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
            await message.channel.send(embed=emb)
        except ApiException as exp:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % exp)


    #meme function
    if message.content.startswith('!meme'):
        res = requests.get("https://memes.blademaker.tv/api?lang=en")
        memes = res.json()
        title = memes['title']
        ups = memes ['ups']
        downs = memes['downs']
        subs = memes['subreddit']
        embed = discord.Embed(title= f"{title}\nSubreddit: {subs}")
        embed.set_image(url=memes['image'])
        embed.set_footer(text = f"👍: {ups} 👎: {downs}")
        await message.channel.send(embed=embed)


    #join vchannel
    if message.content.startswith('!join'):
        channel = message.author.voice.channel
        await channel.connect()


    #leave vchannel
    if message.content.startswith('!leave'):
        server = message.guild
        voice_client = server.voice_client
        await voice_client.disconnect()


    #dictionary
    if message.content.startswith('!find'):
        word = 'Smile'
        ques =  message.content.split(" ")
        if len(ques) > 1:
            s= ' '
            word = s.join(ques[1:])
        if len(ques) <= 2:
            mean = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
            ans = mean.json()
            json_data = json.loads(mean.text) 
            if any('word' in keys for keys in json_data):
                define = json_data[0]['meanings']
                define2 = define[0]['definitions']
                define3= define2[0]['definition']
                define4= define2[0]['example']
                ans = word + '\n' + 'Meaning' + ' :- ' + define3 + '\n' + 'Example :- ' + define4 + '.'
                await message.channel.send(ans)
            else:
                await message.channel.send("Sorry pal, we couldn't find definitions for '" + word + "'. You can head to the web instead.")
        else:
            await message.channel.send('Please type one word at a time!!')


    #roast function
    if message.content.startswith('!roast'):
        await message.channel.send(random.choice(roast_lines))


    #say function
    if message.content.startswith('!say'):
        say = message.content.split(' ')
        if len(say) > 1:
            s = ' '
            final = s.join(say[1:])
            await message.channel.send(final + '\n' + '**- {}**'.format(message.author))
        else:
            await message.channel.send('Hey buddy!!  Wassup?')


    #joke function
    if message.content.startswith('!joke'):
        joke = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,racist,sexist")
        jokes = joke.json()
        json_data = json.loads(joke.text)
        type = json_data["type"]
        if type == 'single':
            joke1 = json_data["joke"]
            await message.channel.send(joke1)
        if type == 'twopart':
            joke2 = json_data["setup"]
            joke3 = json_data["delivery"]
            jokefinal = joke2 + '\n' + joke3
            await message.channel.send(jokefinal)
    #play vmusic
    

client.run(os.getenv('TOKEN'))
