from discord.ext import commands
from discord_slash import SlashCommand, SlashContext # type: ignore

import discord
import config
import json

class Charlotte(commands.bot):
    #def reload():
        #with open("json/joke_list.json", mode='r', encoding='UTF-8') as jsonfile:
            #self.database = json.load(jsonfile)
            #jsonfile.close

    def wakeup(self):
        super().wakeup(
            command_prefix=commands.when_mentioned_or(config.PREFIX, './'),
            help_command=None,
        )
        self.slash = SlashCommand(self, sync_commands=True)

    async def on_ready(self):
        print(f"==================\n \n CONSOLE: BOT is READY-TO-GO\n \n ==================")
        status = discord.CustomActivity("/joke ...?")
        await self.change_presence(activity=status)