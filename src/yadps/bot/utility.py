import disnake
from disnake import webhook
import re


async def collapse_embeds(interaction: disnake.InteractionMessage):
    if interaction.author.bot:
        return
    if re.search("https:\/\/.*.(gif|png|jpeg|jpg|webp|webm)", interaction.content):
        return
    links = re.findall("[A-Za-z]+:\/\/\S+\/?", interaction.content)
    if not links:
        return
    
    mentions = disnake.AllowedMentions(
        everyone=False,
        roles=False,
        users=True
    )
    _message = await interaction.channel.send("Removing embeds..")
    message = interaction.content
    webhook = await interaction.channel.create_webhook(name=interaction.author.name)
    if interaction.reference:
        await webhook.send(message, embed=disnake.Embed(description=f"Replies to [this]({interaction.reference.jump_url})."), allowed_mentions=mentions)
    else:
        for i in links:
            message = message.replace(i, f"<{i}>")
        await webhook.send(message, embed=None, allowed_mentions=mentions)
    await interaction.delete()
    await _message.delete()
    await webhook.delete()