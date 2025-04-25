import interactions
from interactions import Extension, slash_command, SlashContext

import bot
import random

class slashJoke(Extension):
    @slash_command(name="joke", description="ダジャレの呼び声がする……")
    async def joke(self, ctx: SlashContext):
        await ctx.send(bot.DATA[random.randint(1,len(bot.DATA))]["joke"])