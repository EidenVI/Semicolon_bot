import discord
from discord.ext import commands
from discord import app_commands

class Greetings(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # /hello command
    @app_commands.command(name='hello', description="Say hello!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Hey, {interaction.user.mention}!')
        
# setup func
async def setup(client: commands.Bot):
    await client.add_cog(Greetings(client))
