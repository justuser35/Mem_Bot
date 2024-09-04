from disnake.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: int=1):
        if ctx.guild.get_role(1228017255493931119) in ctx.author.roles:
            await ctx.channel.purge(limit=amount+1)
            await ctx.send(f'Удалено {amount} сообщений', delete_after=4)
        else:
            await ctx.send(f"У вас недостаточно прав")


def setup(bot):
    bot.add_cog(Clear(bot))