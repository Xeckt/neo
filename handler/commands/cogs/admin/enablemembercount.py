import time

import disnake
from handler.config.data import Data
from disnake.ext import commands


class EnableMemberCount(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Ban a given user.",
        hidden=True
    )
    @commands.has_any_role(
        data.config["adminRoleId"]
    )
    async def enablemembercount(self, interaction: disnake.ApplicationCommandInteraction, channel: disnake.VoiceChannel):
        count = f"Member count: {interaction.guild.member_count}"
        start_time = time.time()
        if not isinstance(channel, disnake.VoiceChannel):
            await interaction.send("You must supply a voice channel.")
            return
        while True:
            await channel.edit(name=count)
            time.sleep(300.0 - ((time.time() - start_time) % 60.0))
            # Careful of this command, there is no way implemented to stop the loop yet.



def setup(bot):
    bot.add_cog(EnableMemberCount(bot))
