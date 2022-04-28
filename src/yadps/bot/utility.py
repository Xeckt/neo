import disnake
import re


async def collapse_embeds(interaction: disnake.InteractionMessage):
    if not interaction.author.bot:
        if interaction.embeds:
            await interaction.edit(suppress=True)
