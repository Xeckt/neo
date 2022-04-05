import asyncio
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
        description="Enable member count on a supplied voice channel via id.",
        hidden=True
    )
    @commands.has_any_role(
        data.config["adminRoleId"]
    )
    async def enablemembercount(self, interaction: disnake.ApplicationCommandInteraction, channel: disnake.VoiceChannel):
        count_str = f"Member count: {interaction.guild.member_count}"
        count = interaction.guild.member_count
        start_time = time.time()
        if not isinstance(channel, disnake.VoiceChannel):
            await interaction.send("You must supply a voice channel.")
            return
        await interaction.send(f"Enabling member count on channel: {channel.mention}")
        prev_count = count
        while True:
            await channel.edit(name=count_str)
            if count == prev_count:
                continue
            if (count - prev_count) >= 10:
                await interaction.send(f"{interaction.guild.name} has gained 10 more users! Old count: {prev_count} -> "+
                                       f"New count: {count}")
            prev_count = count
            await asyncio.sleep(300 - ((time.time() - start_time) % 60.0))
            # Will implement lock checks for this to make sure a previously enabled async thread isn't active



def setup(bot):
    bot.add_cog(EnableMemberCount(bot))
