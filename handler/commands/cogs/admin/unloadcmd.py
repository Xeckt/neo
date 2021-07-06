from discord.ext import commands
import settings.constants as constants


class Unload(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(
        description="Unload a command module",
        hidden=True
    )
    @commands.has_any_role(constants.ADMIN_ROLE_ID)
    async def unload(self, ctx, command_rank, command):
        if commands.is_owner():
            if command == "load":
                await ctx.send(f"{ctx.author.name} You shouldn't unload the load command.")
                return
            self.bot.unload_extension(f'cogs.commands.{command_rank}.{command}')
            await ctx.channel.send(f"{ctx.author.mention} Unloaded command: {command}")
        else:
            return


def setup(bot):
    bot.add_cog(Unload(bot))
