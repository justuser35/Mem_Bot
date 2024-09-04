import disnake
from disnake.ext import commands

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def rules(self, ctx):
        embed = disnake.Embed(title= '📕Правила нашего сервера 2ИС1❗', description=
        "1. не материться\n"
        "2. не быть ебланом\n"
        "3. быть пивозавром\n"
        "4. перевестись на электрика", color=0x992D22)
        embed.set_image(url='attachment://F56nirpNsMs.jpg')


        await ctx.guild.get_channel(1258561958727258184).send(embed=embed, file=disnake.File('./files/F56nirpNsMs.jpg'))



def setup(bot):
    bot.add_cog(Rules(bot))