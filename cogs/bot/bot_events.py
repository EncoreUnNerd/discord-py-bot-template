import discord

from packages import database, utilities
from discord.ext import commands
from discord.ui import Button, View


class BotEvents(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        print("The bot is successfuly connected !")
        await self.client.tree.sync()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.client.guilds)} servers 👀"))
        await self.client.add_view()
        print(f"The bot {self.client.user} as succesfuly been started !")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        database.delete_server_from_db(guild.id)
        await self.client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.client.guilds)} servers 👀"))

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        database.add_server_in_db(guild.id)
        embed_welcome_message = utilities.create_embed(title="👋 Thank you for adding me",
                                                       description="Im an utility bot, if you don't know how to use me,"
                                                                   " I have a documentation page, you can access it "
                                                                   "by clicking the button below 👇")
        view = View()
        doc = Button(label="Documentation", emoji="📜",
                     url="https://streamy.gitbook.io/streamy-documentation/")
        view.add_item(doc)
        await guild.text_channels[0].send(embed=embed_welcome_message, view=view)
        await self.client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.client.guilds)} servers 👀"))


async def setup(client):
    await client.add_cog(BotEvents(client))
