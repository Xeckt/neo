from disnake.ext import commands
import asyncio
import disnake as discord
from yadps.config.data import Data
from yadps.logging.log import Log

class Polls(commands.Cog):
    """Poll voting system."""

    def __init__(self, bot):
        self.bot = bot
        self.data = Data()
        self.yadps_log = Log().create(__name__, self.data.botLog)

    def to_emoji(self,c):
        base = 0x1f1e6
        return chr(base + c)

    @commands.command()
    @commands.guild_only()
    async def poll(self, ctx, *, question):
        """
        Multiple optioned poll. Only first vote is considered. Timeout of 1 minute
        """
        messages = [ctx.message]
        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and len(m.content) <= 100

        for i in range(20):
            messages.append(await ctx.send(f'Send an option or `post` (`pbf`) to post poll.'))

            try:
                entry = await self.bot.wait_for('message', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                return await ctx.send(embed=discord.Embed(description="Timed out!"), delete_after=3)

            messages.append(entry)

            if entry.clean_content.lower().startswith(f'publishify') or entry.clean_content.lower().startswith(f'pbf'):
                break

            answers.append((self.to_emoji(i), entry.clean_content))

        try:
            await ctx.channel.delete_messages(messages)
        except:
            pass # no perms for gods sake

        answer = '\n'.join(f'{keycap}: {content}' for keycap, content in answers)
        actual_poll = await ctx.send(embed=discord.Embed(title=f'"{question.title()}"',description=f'{answer}',colour=discord.Colour.random()).set_author(name=f"A poll by {ctx.author.name}",icon_url=ctx.author.avatar))
        await actual_poll.edit(embed=discord.Embed(title=f'"{question.title()}"',description=f'{answer}',colour=discord.Colour.random()).set_author(name=f"A poll by {ctx.author.name}",icon_url=ctx.author.avatar).set_footer(text=f"Poll ID: {actual_poll.id}"))
        for emoji, _ in answers:
            await actual_poll.add_reaction(emoji) # AND CHILL
            

    @commands.command(name='tally',help="Get the results of a poll!!")
    @commands.guild_only()
    async def tally(self, ctx, poll_id):
        """Tally the created poll"""
        pid=poll_id
        poll_message = await ctx.message.channel.fetch_message(pid)
        if not poll_message.embeds:
            return await ctx.send("Wrong ID",delete_after=5)
        embed = poll_message.embeds[0]
        if poll_message.author != self.bot.user:
            return await ctx.send("I didn't create that poll!!",delete_after=5)
        if not embed.footer.text.startswith('Poll ID:'):
            return await ctx.send("Wrong Poll ID",delete_after=5)
        unformatted_options = [x.strip() for x in embed.description.split('\n')]
        opt_dict = {x[:2]: x[3:] for x in unformatted_options} if unformatted_options[0][0] == '1' \
            else {x[:1]: x[2:] for x in unformatted_options}
        voters = [self.bot.user.id]

        tally = {x: 0 for x in opt_dict.keys()}
        for reaction in poll_message.reactions:
            if reaction.emoji in opt_dict.keys():
                reactors = await reaction.users().flatten()
                for reactor in reactors:
                    if reactor.id not in voters:
                        tally[reaction.emoji] += 1
                        voters.append(reactor.id)

        output = 'Results of the poll for {}:\n'.format(embed.title) + \
                '\n'.join(['{}: {}'.format(opt_dict[key], tally[key]) for key in tally.keys()])
        await ctx.send(embed=discord.Embed(description=output))

    @commands.command()
    @commands.guild_only()
    async def quickpoll(self, ctx, *questions_and_choices: str):
        if len(questions_and_choices) < 3:
            return await ctx.send('Need at least 1 question with 2 choices.')
        elif len(questions_and_choices) > 21:
            return await ctx.send('You can only have up to 20 choices.')

        perms = ctx.channel.permissions_for(ctx.me)
        if not (perms.read_message_history or perms.add_reactions):
            return await ctx.send('Need Read Message History and Add Reactions permissions.')

        question = questions_and_choices[0]
        choices = [(to_emoji(e), v) for e, v in enumerate(questions_and_choices[1:])]

        try:
            await ctx.message.delete()
        except:
            pass

        body = "\n".join(f"{key}: {c}" for key, c in choices)
        poll = await ctx.send(f'{ctx.author} asks: {question}\n\n{body}')
        for emoji, _ in choices:
            await poll.add_reaction(emoji)

def setup(bot):
    bot.add_cog(Polls(bot))