import disnake
from disnake import webhook
import re


async def collapse_embeds(interaction: disnake.InteractionMessage):
    if interaction.author.bot:
        return
    if re.search("https:\/\/.*.(gif|png|jpeg|jpg|webp|webm)", interaction.content):
        return
    links = re.findall("[A-Za-z]+:\/\/\S+\/?", interaction.content)
    if links:
        _message = await interaction.channel.send("Removing embeds..")
        message = interaction.content
        for i in links:
            message = message.replace(i, f"<{i}>")
        webhook = await interaction.channel.create_webhook(name=interaction.author.name)
        await webhook.send(message, embed=None)
        await interaction.delete()
        await _message.delete()
        await webhook.delete()