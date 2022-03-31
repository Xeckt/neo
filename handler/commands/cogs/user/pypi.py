import disnake
import requests
from disnake.ext import commands
from handler.config.data import Data


class PyPi(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Get information on a pypi package.",
    )
    @commands.has_any_role(
        data.config["memberRoleId"]
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def pypi(self, inter: disnake.ApplicationCommandInteraction, package):
        print(f'https://pypi.org/pypi/{package}/json')
        r = requests.get(f"https://pypi.org/pypi/{package}/json")
        if r.status_code != 200:
            embed = disnake.Embed(
                title="Not found"
            )
            await inter.send(embed=embed)
            return
        r = r.json()
        embed = disnake.Embed(
            title=f"{package} v{r.get('info').get('version')}",
            description=f"{r.get('info').get('summary')}"
        )
        fields = {
            'Author': 'author',
            'Author Email': 'author_email',
            'Discontinued': 'yanked',
            'Keywords': 'keywords',
            'Bugs': 'bugtrack_url',
            'Project URL': 'project_url',
        }
        for name, value in fields.items():
            if r.get('info').get(value):
                embed.add_field(name, r.get('info').get(value))
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(PyPi(bot))
