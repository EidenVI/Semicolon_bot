import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()
CREATOR_ID = os.getenv('CREATOR_ID')

class ServerMenu(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        
    @app_commands.command(name='server_menu', description='Displays the server menu message')
    @app_commands.checks.has_role(1262430755410415688)
    async def menu_first(self, interaction: discord.Interaction):
            if interaction.user.id != int(CREATOR_ID):
                await interaction.response.send_message(f"You don't have the necessary permission to do that.", ephemeral=True)
                return
            embed = discord.Embed(title="Welcome to Our Community!", description=("We are delighted to have you join us."), color=0x5865F2)
            await interaction.response.send_message(embed=embed)


async def setup(client: commands.Bot):
    await client.add_cog(ServerMenu(client))