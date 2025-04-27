from interactions import Extension, slash_command, SlashContext
from internal.loader import Loader
import random

# データを取得
data = Loader.get_data()

class slashJoke(Extension):
    @slash_command(name="joke", description="ダジャレの呼び声がする……")
    async def joke(self, ctx: SlashContext):
        await ctx.send(data[str(random.randint(1,len(data)-1))]["joke"])