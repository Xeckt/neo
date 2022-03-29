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

        embed.add_field("Author", r.get("info").get("author"))
        embed.add_field("Email", r.get("info").get("author_email"))
        embed.add_field("Discontinued", r.get("info").get("yanked"))
        embed.add_field("Keywords", r.get("info").get("keywords"))
        embed.add_field("URL", f"[{package}]({r.get('info').get('project_url')})")
        if r.get('info').get('bugtrack_url'):
            embed.add_field("Bugs", f"[Click Here]({r.get('info').get('bugtrack_url')})")
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(PyPi(bot))
