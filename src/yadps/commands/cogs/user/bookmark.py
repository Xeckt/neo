import requests
import disnake
from disnake.ext import commands
from yadps.config.data import Data

class BookMark(commands.Cog):

    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(aliases=["bm"])
    async def bookmark(self, ctx: commands.Context, name: str="bookmark"):
        if not ctx.message.reference:
            embed = disnake.Embed(
                title="Error",
                description="You must reply to the message you want to bookmark."
            )
            await ctx.reply(embed=embed)
            return
        embed = disnake.Embed(
            title=name,
            description=f"[click here]({ctx.message.reference.jump_url})"
        )
        await ctx.author.send(embed=embed)
    
    
def setup(bot):
    bot.add_cog(BookMark(bot))
