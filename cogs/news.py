from disnake.ext import commands
import disnake
from bs4 import BeautifulSoup as bs
import requests

html_text = requests.get("https://habr.com/ru/news/").text
list = []
soup = bs(html_text, 'lxml')
articles = soup.find_all('a', class_="tm-title__link")

# сюда надо бд прикрутить и будем хранить старые статьи потом при обновлении страницы будем сравнивать значения из базы и тут, если разные то публикуем.

# get text y статей


for article in articles:
    title = article.find("span").text
    list += title + article.get('href') # name and link


class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.a = soup.find_all
    @commands.slash_command(
        name="news",
        description="Создать новую публикацию новости"
    )
    async def news(
            self,
            inter: disnake.ApplicationCommandInteraction,
            title: str,
            content: str
    ):
        forum_channel = self.bot.get_channel(1273315053067567154)
        try:
            await forum_channel.create_thread(
                name=title,
                content=content
            )
            await inter.response.send_message("Публикация создана!", ephemeral=True)
        except Exception as e:
            await inter.response.send_message(f'Тип {type(e)}, ошибка {Exception}', ephemeral=True)


def setup(bot):
    bot.add_cog(News(bot))