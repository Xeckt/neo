from yadps.logging.log import Log
from yadps.config.data import Data
import requests
import disnake
from disnake.ext import commands


class Emojis(commands.Cog):

    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Add emojis to a server",
        hidden=True
    )
    @commands.has_any_role(
        data.adminRoleId
    )
    async def emojiadd(self, inter: disnake.ApplicationCommandInteraction, emoji_name: str, emoji_url: str):
        try:
            r = requests.get(emoji_url)
        except:
            await inter.send("Invalid emoji URL.")
        try:
            emoji = await inter.guild.create_custom_emoji(name="test", image=r.content)
            if emoji.animated:
                await inter.send(f"Success: <a:{emoji.name}:{emoji.id}>.")
            else:
                await inter.send(f"Success: <:{emoji.name}:{emoji.id}>.")
        except Exception as e:
            await inter.send(f"Error: {e}")

    @commands.slash_command(
        description="Delete emojis from a server.",
        hidden=False
    )
    @commands.has_any_role(
        data.adminRoleId
    )
    async def emojidelete(self, inter: disnake.ApplicationCommandInteraction, emoji: disnake.Emoji):
        try:
            await inter.guild.delete_emoji(emoji)
        except Exception as e:
            await inter.send(f"Error: {e}")
        await inter.send("Success.")

    @commands.slash_command(
        description="Add stickers to a server",
        hidden=True
    )
    @commands.has_any_role(
        data.adminRoleId
    )
    async def stickeradd(self, inter: disnake.ApplicationCommandInteraction, sticker_name: str, sticker_emoji: str, sticker_url: str):
        await inter.response.defer()
        try:
            r = requests.get(sticker_url)
            print(r.status_code)
        except:
            await inter.send("Invalid URL.")
        try:
            with open('./temp_file', "wb") as f:
                f.write(r.content)
        except Exception as e:
            await inter.send(f"Error while creating file: {e}")
        file = disnake.File('./temp_file')
        try:
            await inter.guild.create_sticker(name=sticker_name, emoji=sticker_emoji, file=file)
            await inter.send("Created sticker.")
        except Exception as e:
            await inter.send(f"Error while creating sticker: {e}")
            
def setup(bot):
    bot.add_cog(Emojis(bot))
