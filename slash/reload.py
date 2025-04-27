from interactions import Extension, slash_command, SlashContext
from internal.loader import Loader
import random

class slashReload(Extension):
    @slash_command(name="reload", description="dbを再読み込み(非常用)")
    async def reload(self, ctx: SlashContext):
        Loader.get_data()
        print("CONSOLE: cmd /reload called.")
        response_list = [
            "ダジャレを読み込むのは、見込むセンスのある者だからこそすることよ。",
            "ダジャレを記した手帳は不要……書き込む手間が惜しいわ。",
            "ダジャレは生活のエッセンスなの。派生するし、センスが問われるわ。"
        ]
        await ctx.send(random.choices(response_list))