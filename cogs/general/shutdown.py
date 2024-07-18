import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()
CREATOR_ID = os.getenv('CREATOR_ID')

class Shutdown(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        
    # /shutdown command
    @app_commands.command(name='shutdown', description="Shut down a Semicolon")
    @app_commands.checks.has_role(1262430755410415688)
    async def shutdown(self, interaction: discord.Interaction):
        if interaction.user.id != int(CREATOR_ID):
            await interaction.response.send_message(f"You don't have the necessary permission to do that.", ephemeral=True)
            return
        await interaction.response.send_message("I'll be back...")
        await self.client.close()
        return

# setup func
async def setup(client: commands.Bot):
    await client.add_cog(Shutdown(client))
