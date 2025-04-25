import interactions
import discord
from discord.ext import commands
from interactions import listen
from interactions.api.events import Startup

import config
import json

def dbReload():
    with open("json/joke_list.json", mode='r', encoding='UTF-8') as jsonfile:
        db = json.load(jsonfile)
        jsonfile.close

class Charlotte(interactions.Client):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(config.PREFIX, './'),
            help_command=None,
        )
        db = dbReload()

    @listen(Startup)
    async def on_startup(self): 
        print(f" ==================\n \n CONSOLE: CLIENT is READY-TO-GO\n This bot is owned by {self.owner}\n \n ==================")
        status = discord.CustomActivity("/joke ...?")
        await self.change_presence(activity=status)