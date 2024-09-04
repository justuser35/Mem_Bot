from disnake.ext import commands
import disnake


class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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