import disnake
from disnake.ext import commands
from yadps.config.data import Data
import yaml


class Tags(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot
        with open('settings/tags.yaml') as file:
            self.tags = yaml.load(file, Loader=yaml.loader.Loader)
        self.tag_list = [i for i in self.tags['tags']]

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Show a tag.",
    )
    @commands.has_any_role(
        data.memberRoleId
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def tags(self, inter: disnake.ApplicationCommandInteraction, tag: str = None):

        if not tag:
            embed = disnake.Embed(
                title="All tags",
                description="\n".join([i for i in self.tags['tags']])
            )
            await inter.send(embed=embed)
            return
        try:
            embed = disnake.Embed(
                title=self.tags['tags'][tag]['title'],
                description=self.tags['tags'][tag]['description']
            )
            await inter.send(embed=embed)
        except KeyError:
            embed = disnake.Embed(
                title="That tag doesn't exist"
            )
            await inter.send(embed=embed)

    @tags.autocomplete("tag")
    async def autocomplete_tags(self, inter: disnake.ApplicationCommandInteraction, user_input: str):
        return [i for i in self.tag_list if user_input in i.lower()]


def setup(bot):
    bot.add_cog(Tags(bot))
