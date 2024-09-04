import disnake
import os
from disnake.ext import tasks, commands
import config
import vk_api
import random

class CheckPosts(commands.Cog):
    def __init__(self, bot, vk):
        self.bot = bot
        self.vk = vk
        self.last_post_id = None
        self.check_vk_posts.start()

    @tasks.loop(seconds=15)
    async def check_vk_posts(self):
        try:
            posts = self.vk.wall.get(owner_id=config.GROUP_ID, count=1)['items']
            if posts:
                post = posts[0]
                post_id = post['id']

                if self.last_post_id == None:
                    self.last_post_id = post_id

                else:
                    if post_id != self.last_post_id:
                        self.last_post_id = post_id
                        message = post.get('text', 'Нет текста')
                        attachments = post.get('attachments', [])

                        images = []
                        for attachment in attachments:
                            if attachment['type'] == 'photo':
                                photo = attachment['photo']
                                image_url = photo['sizes'][-1]['url']
                                images.append(image_url)

                        embed = disnake.Embed(
                            title=message,
                            color=0x00222222
                        )

                        button = disnake.ui.Button(
                            label="Изменить цвет",
                            style=disnake.ButtonStyle.primary,
                            custom_id="change_color_button"
                        )

                        view = disnake.ui.View()
                        view.add_item(button)

                        if images:
                            embed.set_image(url=images[0])
                            if len(images) > 1:
                                for index, image_url in enumerate(images[1:], start=2):
                                    embed.add_field(name=f"Изображение {index}", value=image_url, inline=False)

                        channel = self.bot.get_channel(1257681163707748416)
                        if channel:  # Check if the channel exists
                            await channel.send(embed=embed, view=view)
                        else:
                            print("Channel not found.")

        except Exception as e:
            print(f'Error checking VK posts: {e}')

    @commands.Cog.listener("on_button_click")
    async def button_click(self, interaction: disnake.MessageInteraction):
        if interaction.component.custom_id == "change_color_button":
            new_color = disnake.Color.from_rgb(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            new_embed = interaction.message.embeds[0]
            new_embed.color = new_color
            await interaction.response.edit_message(embed=new_embed)

    @check_vk_posts.before_loop
    async def before_check_vk_posts(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(CheckPosts(bot, bot.vk))