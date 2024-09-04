import disnake
import vk_api
import requests
import config
from disnake.ext import commands
from disnake.ext import tasks
from io import BytesIO
import os

# ЗАДАЧИ

#1. каждую минуту проверять количество участников и изменять название голосового канала
#2.


VK_ACCESS_TOKEN = '5efe4dc85efe4dc85efe4dc8405de7f4f055efe5efe4dc83864a2ad96aac8e554743ff3'

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), test_guilds=[1257681163707748412])
bot.remove_command("help")

vk_session = vk_api.VkApi(token=VK_ACCESS_TOKEN)
vk = vk_session.get_api()

bot.config = config
bot.vk = vk

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.command(name="reload", aliases=["r", "rel"])
async def reload(ctx):
    if ctx.author.id == 703135070667407440:
        await ctx.message.delete()
        extensions = list(bot.extensions)
        for extension in extensions:
            bot.unload_extension(extension)

        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                extension = f"cogs.{file[:-3]}"
                try:
                    bot.load_extension(extension)
                except Exception as e:
                    print(f'[─] {extension} - {e}')
        await ctx.send("коги перезагружены")
    else:
        await ctx.send("У ВАС НЕТ ПРАВ")
        await ctx.send("https://media1.tenor.com/m/EKWnxlK2BH0AAAAC/byuntear-bob-sponge.gif")


@bot.event
async def on_ready():
    print(f'Бот в сети: {bot.user.name}')


bot.run(config.TOKEN)