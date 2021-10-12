import discord
#import os
import json
from discord.channel import VoiceChannel
import requests
import random
import giphy_client
from giphy_client.rest import ApiException
from discord.ext import commands


class api(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def meme(self , ctx):
        r = requests.get("https://memes.blademaker.tv/api?lang=en")
        res = r.json()
        title = res["title"]
        ups = res["ups"]
        downs = res["downs"]
        sub = res["subreddit"]
        m = discord.Embed(title = f"{title}\nSubreddit: {sub}")
        m.set_image(url = res["image"])
        m.set_footer(text = f"👍 : {ups} 👎 : {downs}")
def setup(bot):
    bot.add_cog(api(bot))