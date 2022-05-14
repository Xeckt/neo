import disnake
from disnake.ext import commands
from yadps.config.data import Data


class Lore(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot: disnake.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Add lore to the mighty guild.",
    )
    @commands.has_any_role(
        data.memberRoleId
    )
    @commands.cooldown(1, 30*60, commands.BucketType.guild)
    async def lore(self, inter: disnake.ApplicationCommandInteraction, title, desc, image_url):
        data = Data()
        lore_embed = disnake.Embed(
            title=title,
            description=desc,
        )
        if len(image_url) != 0:
            lore_embed.set_image(url=image_url)
        channel = await self.bot.fetch_channel(data.loreChannel)
        await channel.send(embed=lore_embed)
        await inter.send("Posted.")


def setup(bot):
    bot.add_cog(Lore(bot))