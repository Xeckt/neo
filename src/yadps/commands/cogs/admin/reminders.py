import asyncio

import disnake
from yadps.config.data import Data
from disnake.ext import commands


class Reminders(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot
        self.reminder = False

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        for i in message.embeds:
            if i.description:
                if "Bump done" in i.description and self.reminder:
                    channel = await self.bot.fetch_channel(message.channel.id)
                    msg = await channel.fetch_message(message.id)
                    embed = disnake.Embed(
                        title="Thanks for bumping!"
                    )
                    await msg.reply(embed=embed)
                    await asyncio.sleep(2*60*60)
                    embed = disnake.Embed(
                        title="Bump us!",
                        description="""
                        Bumping helps the server grow. You can bump a server every 2 hours.
                        To bump a server, type `/bump`. You can also go [here](https://disboard.org/server/956780366063095808) to bump us!
                        Note that `/bump` is a slash command and not a text based command.
                        """
                    )
                    await channel.send(embed=embed, delete_after=2*60*60)


    @commands.slash_command(
        description="Send a message to a channel reminding to bump every 2 hours.",
        hidden=True
    )
    @commands.has_any_role(
        data.config["adminRoleId"]
    )
    async def bump(self, interaction: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel):
        if not isinstance(channel, disnake.TextChannel):
            await interaction.send("You must supply a text channel.")
            return
        
        if self.reminder:
            self.reminder = False
            await interaction.send(f"disabling bump reminders on channel: {channel.mention}")
            return
        await interaction.send(f"Enabling bump reminders on channel: {channel.mention}")
        self.reminder = True        


def setup(bot):
    bot.add_cog(Reminders(bot))
