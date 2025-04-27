from interactions import Extension, slash_command, SlashContext, Option
from internal.loader import Loader
import json
import os
from datetime import datetime

class slashAdd(Extension):
    @slash_command(
        name="add",
        description="新しいダジャレを……！？",
        options=[
            Option(name="joke", description="追加するダジャレ", type=str, required=True),
        ],
    )
    async def add(self, ctx: SlashContext, joke: str):
        # データをロード
        data = Loader.get_data()
        # 新しいキーを生成（既存のキーの最大値 + 1）
        new_key = str(max(map(int, data.keys())) + 1) if data else "1"
        author = ctx.author.display_name
        date = datetime.now().strftime("%Y/%m/%d")

        # 一時的記憶
        data[new_key] = {
            "joke": joke,
            "rating": 0,
            "author": author,
            "date": date,
        }

        # JSON ファイルに保存
        json_path = os.path.join(os.path.dirname(__file__), "../json/joke_list.json")
        with open(json_path, mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        
        await ctx.send(f"新しいダジャレを追加！\n`「{joke}」` by {author}")