import disnake
import re


async def collapse_embeds(interaction: disnake.InteractionMessage):
    if not interaction.author.bot:
        if interaction.embeds and not re.search("https:\/\/.*.gif", interaction.content):
            await interaction.edit()
