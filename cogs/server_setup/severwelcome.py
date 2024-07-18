import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()
CREATOR_ID = os.getenv('CREATOR_ID')

class Serverwelcome(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        
    @app_commands.command(name='welcome_menu', description='displays the community welcome message')
    @app_commands.checks.has_role(1262430755410415688)
    async def menu_first(self, interaction: discord.Interaction):
        if interaction.user.id != int(CREATOR_ID):
            await interaction.response.send_message(f"You don't have the necessary permission to do that.", ephemeral=True)
            return
        embed = discord.Embed(title="Welcome to Our Community!", description=(
            "We are delighted to have you join us. This server is a place for people from all over the world to connect, "
            "share ideas, and have fun. Whether you're here to chat, collaborate, or just hang out, you're in the right place!\n\n"
            "Make sure to personalize your server profile and check out the #rules-and-info channel for more details.\n\n"
            "Enjoy your stay and let's make this community great together!"
        ), color=0x5865F2)
        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(Serverwelcome(client))