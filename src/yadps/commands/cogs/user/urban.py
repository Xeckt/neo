from disnake.ext import commands
from src.yadps.config.data import Data
import disnake
import requests
import bs4


class Urban(commands.Cog):

    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(description="Find the definition of something from urban dictionary.")
    @commands.has_any_role(
        data.config["memberRoleId"]
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def urban(self, inter: disnake.ApplicationCommandInteraction, query: str):
        r = requests.get(
            f"https://www.urbandictionary.com/define.php?term={query.replace(' ', '+')}")
        if r.status_code == 404:
            embed = disnake.Embed(
                title="404, Not Found",
                description="Your query was not found."
            )
            await inter.send(embed=embed)
            return
        elif r.status_code == 200:
            soup = bs4.BeautifulSoup(str(r.content), 'html5lib')
            embed = disnake.Embed()
            if soup.find("meta", {"property": "og:title"}).get("content"):
                embed.title = soup.find("meta", {"property": "og:title"}).get(
                    "content").replace("Urban Dictionary:", "")
            if soup.find("meta", {"property": "og:description"}).get("content"):
                embed.description = soup.find(
                    "meta", {"property": "og:description"}).get("content")
            await inter.send(embed=embed)
            return
        embed = disnake.Embed(title=f"Something went wrong, {r.status_code}")
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Urban(bot))
