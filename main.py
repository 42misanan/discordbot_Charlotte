from bot import Charlotte
import config

bot = Charlotte()

TOKEN = config.DISCORD_TOKEN

extensions = [
    #"cogs.admin",
    #"cogs.check",
    #"slash.vq",
    #"slash.point",
    #"slash.rank",
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(TOKEN)