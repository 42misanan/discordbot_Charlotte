import interactions
import discord
from discord.ext import commands
from interactions import listen
from interactions.api.events import Startup

import config
from internal.loader import Loader

class Charlotte(interactions.Client):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(config.PREFIX, './'),
            help_command=None,
        )

    @listen(Startup)
    async def on_startup(self): 
        print(f"==================\n"
            "\n"
            "CONSOLE: TOKEN AUTHENTICATION SUCCESSFUL\n"
            f"bot 'Charlotte (Unofficial)' is owned by {self.owner}\n"
            "\n"
            "==================")
        status = discord.CustomActivity("/joke ...?")
        await self.change_presence(activity=status)