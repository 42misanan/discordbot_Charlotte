from interactions import Extension, slash_command, SlashContext
from internal.loader import Loader
import random

# データを取得

class slashJoke(Extension):
    @slash_command(name="joke", description="ダジャレの呼び声がする……")
    async def joke(self, ctx: SlashContext):
        # 現在の db および key を取得
        data = Loader.get_data()
        keys = list(data.keys())
        if not keys:
            await ctx.send("ダジャレが……思いつかない……？そんなっ……！")
            return
        #random_keyは一度出したら固定
        random_key = random.choice(keys)
        joke = (data[random_key].get("joke", "None"))
        rating = (data[random_key].get("rating", "None"))
        date = (data[random_key].get("date", "None"))
        # ダジャレを送信
        await ctx.send(f"**{joke}**\n"
                        "```\n"
#                        f"評価:{rating}\n"
#                        f"登録:{date}\n"
                        "```")