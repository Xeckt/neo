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
        if not isinstance(channel, disnake.VoiceChannel):
            await interaction.send("You must supply a voice channel.")
            return
        await interaction.send(f"Enabling member count on channel: {channel.mention}")
        prev_count = count
        while True:
            if (count - prev_count) >= 10:
                await interaction.send(f"{interaction.guild.name} has gained 10 more users! Old count: {prev_count} -> "+
                                       f"New count: {count}")
            await channel.edit(name=count_str)
            await interaction.send(f"Count updated from: {prev_count} to {count}")
            prev_count = count
            await asyncio.sleep(3600) # 1 hour



def setup(bot):
    bot.add_cog(EnableMemberCount(bot))
