import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()
CREATOR_ID = os.getenv('CREATOR_ID')

class Repeat(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        
    # /say command
    @app_commands.command(name='say', description="Repeat after me!")
    @app_commands.describe(args='What should I say?')
    async def say(self, interaction: discord.Interaction, args: str):
        await interaction.response.send_message(args)
    
# setup func
async def setup(client: commands.Bot):
    await client.add_cog(Repeat(client))
