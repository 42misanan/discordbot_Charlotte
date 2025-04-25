import interactions
from interactions import utils

import discord
import config
import json

class Charlotte(interactions.Client):
    #def reload():
        #with open("json/joke_list.json", mode='r', encoding='UTF-8') as jsonfile:
            #self.database = json.load(jsonfile)
            #jsonfile.close

    def wakeup(self):
        super().wakeup(
            command_prefix=utils.when_mentioned_or(config.PREFIX, './'),
            help_command=None,
        )
        self.slash = interactions.SlashCommand(self, sync_commands=True)

    #async def on_startup(self): 
        #print("==================\n \n CONSOLE: CLIENT is READY-TO-GO\n \n ==================")
        #status = discord.CustomActivity("/joke ...?")
        #await self.change_presence(activity=status)