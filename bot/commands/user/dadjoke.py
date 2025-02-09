import requests
import disnake
import globals
from disnake.ext import commands

class DadJoke(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(description="Retrieve a dad joke!")
    @commands.has_any_role(globals.neo_config.memberRoleId)
    async def dadjoke(self, inter: disnake.ApplicationCommandInteraction):
        request = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
        joke = request.json()["joke"]
        await inter.send(joke)
    
def setup(bot):
    bot.add_cog(DadJoke(bot))
