import disnake
from disnake.ext import commands

class MembersCount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_members_number_update()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        current_members_number = (f"ᴍᴇᴍʙᴇʀꜱ・{sum(1 for member in member.guild.members if not member.bot)}")
        channel = member.guild.get_channel(1273275388230893588)
        await channel.edit(name=current_members_number)


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        current_members_number = (f"ᴍᴇᴍʙᴇʀꜱ・{sum(1 for member in member.guild.members if not member.bot)}")
        channel = member.guild.get_channel(1273275388230893588)
        await channel.edit(name=current_members_number)


    async def update_channel_name(self, guild):
        current_members_number = f"ᴍᴇᴍʙᴇʀꜱ・{sum(1 for member in guild.members if not member.bot)}"
        channel = guild.get_channel(1273275388230893588)
        if channel and isinstance(channel, disnake.VoiceChannel):
            await channel.edit(name=current_members_number)

    def current_members_number_update(self):
        for guild in self.bot.guilds:
            self.bot.loop.create_task(self.update_channel_name(guild))

def setup(bot):
    bot.add_cog(MembersCount(bot))