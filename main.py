import asyncio
import config
import discord
import os
from discord import Embed, app_commands
from discord.app_commands import errors
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix=">",
                      status=discord.Status.online,
                      intents=intents,
                      activity=discord.Activity(type=discord.ActivityType.listening, name=f"documentation"),
                      )


# @client.tree.error
# async def on_error(ctx, error):
#     if isinstance(errors, app_commands.errors.MissingPermissions):
#         e = Embed(
#             title="Tu n'as pas la permissions necessaire pour executer cette commande !",
#             color=0xfefefe
#         )
#         await ctx.response.send_message(embed=e, ephemeral=True)
#     elif isinstance(errors, app_commands.errors.MissingRole):
#         e = Embed(
#             title="Tu n'as pas le role necessaire pour executer cette commade !",
#             color=0xfefefe
#         )
#         await ctx.response.send_message(embed=e, ephemeral=True)
#     else:
#         print(error)


async def load_extensions():
    number_of_cogs_loaded = 0
    for root, dirs, files in os.walk('./cogs'):
        for file in files:
            if file.endswith('.py'):
                cog_path = os.path.join(root, file)
                extension = cog_path.replace('/', '.').replace('\\', '.')[2:-3]
                await client.load_extension(extension)
                number_of_cogs_loaded += 1
    print(f"{number_of_cogs_loaded} Cogs loaded")


async def main():
    async with client:
        print("cogs loading..")
        await load_extensions()
        await client.start(config.TOKEN)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nBOT STOP")
