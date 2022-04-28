import disnake
import re


async def collapse_embeds(interaction: disnake.InteractionMessage):
    if not interaction.author.bot:
        if not (re.search("https://.*(.gif|.mp4|.webp|.png|.jpeg|.jpg)", interaction.content) or re.search("<:.*:.*>", interaction.content) or re.search("<a:.*:.*>", interaction.content)):
            await interaction.edit(suppress=True)
            return
