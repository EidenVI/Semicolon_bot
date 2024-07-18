import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # /help command
    @app_commands.command(name='help', description="Display help information")
    async def help(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="Help",
            description="List of available commands",
            color=0xfcb500
        )

        # Categorize commands
        general_commands = []
        moderation_commands = []

        for command in self.client.tree.walk_commands():
            if command.parent is None:
                if command.name in ["hello", "say"]:
                    general_commands.append(f"/{command.name} - {command.description}")
                elif command.name in ["ban", "unban", "kick"]:
                    moderation_commands.append(f"/{command.name} - {command.description}")

        # Add fields to the embed
        embed.add_field(
            name="General Commands",
            value="\n".join(general_commands),
            inline=False
        )
        embed.add_field(
            name="Moderation Commands",
            value="\n".join(moderation_commands),
            inline=False
        )

        # Send the embed
        await interaction.response.send_message(embed=embed, ephemeral=True)

# setup func
async def setup(client: commands.Bot) -> None:
    await client.add_cog(Help(client))