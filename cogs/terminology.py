from disnake.ext import commands
import disnake


class Terminology(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="term",
        description="Создать новую публикацию термина"
    )
    async def term(
            self,
            inter: disnake.ApplicationCommandInteraction,
            title: str,
            content: str,
    ):
        forum_channel = self.bot.get_channel(1273315339005853737)
        try:
            await forum_channel.create_thread(
                name=title,
                content=content
            )
            await inter.response.send_message("Публикация создана!", ephemeral=True)
        except Exception as e:
            await inter.response.send_message(f'Тип {type(e)}, ошибка {Exception}', ephemeral=True)


def setup(bot):
    bot.add_cog(Terminology(bot))