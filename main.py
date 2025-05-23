from bot import Charlotte
import config

bot = Charlotte()

TOKEN = config.DISCORD_TOKEN

extensions = [
    "slash.add",
    "slash.joke",
    "slash.reload"
]
for extension in extensions:
    bot.load_extension(extension)

bot.start(TOKEN)