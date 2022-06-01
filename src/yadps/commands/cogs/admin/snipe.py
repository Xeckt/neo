import disnake as discord
from disnake.ext import commands
from yadps.config.data import Data
from yadps.logging.log import Log



class Menu(discord.ui.View):
	# Directly taken from @DisnakeDev/disnake -> /examples/views/button/paginator.py
    def __init__(self, embeds: List[discord.Embed]):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.embed_count = 0

        self.first_page.disabled = True
        self.prev_page.disabled = True

        # Sets the footer of the embeds with their respective page numbers.
        for i, embed in enumerate(self.embeds):
            embed.set_footer(text=f"Page {i + 1} of {len(self.embeds)}")

    @discord.ui.button(emoji="⏪", style=discord.ButtonStyle.blurple)
    async def first_page(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        self.embed_count = 0
        embed = self.embeds[self.embed_count]
        embed.set_footer(text=f"Page 1 of {len(self.embeds)}")

        self.first_page.disabled = True
        self.prev_page.disabled = True
        self.next_page.disabled = False
        self.last_page.disabled = False
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(emoji="◀", style=discord.ButtonStyle.secondary)
    async def prev_page(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        self.embed_count -= 1
        embed = self.embeds[self.embed_count]

        self.next_page.disabled = False
        self.last_page.disabled = False
        if self.embed_count == 0:
            self.first_page.disabled = True
            self.prev_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(emoji="❌", style=discord.ButtonStyle.red)
    async def remove(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        await interaction.response.edit_message(view=None)

    @discord.ui.button(emoji="▶", style=discord.ButtonStyle.secondary)
    async def next_page(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        self.embed_count += 1
        embed = self.embeds[self.embed_count]

        self.first_page.disabled = False
        self.prev_page.disabled = False
        if self.embed_count == len(self.embeds) - 1:
            self.next_page.disabled = True
            self.last_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(emoji="⏩", style=discord.ButtonStyle.blurple)
    async def last_page(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        self.embed_count = len(self.embeds) - 1
        embed = self.embeds[self.embed_count]

        self.first_page.disabled = False
        self.prev_page.disabled = False
        self.next_page.disabled = True
        self.last_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)


        
       
        


class Snipe(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot
        self.yadps_log = Log().create(__name__, self.data.botLog)
        self.lastmsg = {}

        
        
        
	def generate_snipe_embed(self,ctx,guild):
        # nostalgic stuff 😥
		eb = []
		try:
			snipes = self.lastmsg[guild]
		except KeyError:
			self.lastmsg.update({guild:[]})
			return []
		if snipes==[]:
			return []
		i=0
		for m in snipes:
			i+=1
			embed = discord.Embed(title=f"Snipe {i}/{len(snipes)}")
			embed.add_field(name="Author", value=m.author.mention,inline=False)
			embed.add_field(name="Message",value=f"{m.content}\n",inline=False)
			embed.add_field(name="Channel",value=m.channel.mention,inline=False)
			embed.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
			eb.append(embed)
		return eb[::-1]

    
    
    @commands.Cog.listener()
    async def on_ready(self):
        pass
    

    
    @commands.Cog.listener()
	async def on_message_delete(self,message:discord.Message):
		if message.author.bot is True:
			return
		try:
			self.lastmsg[message.guild.id].append(message)
		except KeyError:
			self.lastmsg.update({message.guild.id:[]})
			self.lastmsg[message.guild.id].append(message)


    
    
    @commands.command(help="Snipe deleted messages!")
    @commands.has_any_role(data.adminRoleId)
    async def snipe(self, ctx):
        snipe_embeds = self.generate_snipe_embeds(ctx,ctx.guild.id)
		if snipe_embeds is []:
			return await ctx.send("***There is no message to snipe!! Most Likely it's not in my Hitman's Range (Cache) :frowning:...***",delete_after=5)
        await ctx.send(embed=snipe_embeds[0], view=Menu(snipe_embeds))


        
def setup(bot):
    bot.add_cog(Snipe(bot))


