import config
import discord
from discord import app_commands, Embed
from discord.ext import commands


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @app_commands.command(name="ping", description="know if the bot is alright")
    @app_commands.checks.has_permissions(administrator=True)
    async def ping(self, interaction: discord.interactions):
        e = Embed(
            title=f'🏓 Actual ping of the bot : {round(self.client.latency * 1000)}ms',
            color=config.colorBot
        )

        await interaction.response.send_message(embed=e)


async def setup(client):
    await client.add_cog(Ping(client))
