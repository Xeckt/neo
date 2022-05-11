import asyncio
import re

import disnake
from yadps.config.data import Data
from disnake.ext import commands


class Utils(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot
        self.channel = 956780367526899712
        self.reminder = asyncio.Event()
        self.reminder.set()

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.fetch_channel(self.channel)
        embed = disnake.Embed(
            title="Welcome!",
            description="Here are some channels to help you get started:\n<#966124424719892491> : Take your self roles from here.\n<#956780367392698414> : Read the rules and the guidelines on how to ask for help.\n<#957058222248828968> : You can ask for programming related help here.\n<#972542371738816572> : Want to start conversation on a topic? Just start a thread!"
        )
        await channel.send(f"{member.mention}", embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author.bot:
            for i in message.embeds:
                if i.description:
                    if "Bump done" in i.description and self.reminder.is_set():
                        channel = await self.bot.fetch_channel(message.channel.id)
                        msg = await channel.fetch_message(message.id)
                        embed = disnake.Embed(
                            title="Thanks for bumping!"
                        )
                        await msg.reply(embed=embed)
                        await asyncio.sleep(2*60*60)
                        embed = disnake.Embed(
                            title="Bump us!",
                            description=
                            """
                            Bumping helps the server grow. You can bump a server every 2 hours.
                            To bump a server, type `/bump`. You can also go [here](https://disboard.org/server/956780366063095808) to bump us!
                            Note that `/bump` is a slash command and not a text based command.
                            """
                        )
                        await channel.send(embed=embed, delete_after=2*60*60)
            return

    @commands.slash_command(
        description="Send a message to a channel reminding to bump every 2 hours.",
        hidden=True
    )
    @commands.has_any_role(
        data.adminRoleId
    )
    async def bump(self, interaction: disnake.ApplicationCommandInteraction):
        if self.reminder.is_set():
            self.reminder.clear()
            await interaction.send(f"Disabled bump reminders.")
            return
        self.reminder.set()
        await interaction.send(f"Enabled bump reminders.")


def setup(bot):
    bot.add_cog(Utils(bot))
