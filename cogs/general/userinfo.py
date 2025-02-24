import discord
from discord.ext import commands
from discord import app_commands

class UserInfo(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @app_commands.command(name="userinfo", description="Displays information about a user")
    @app_commands.describe(member="The user to view")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
        """Get information about a user"""
        if member is None:
            member = interaction.user

        embed = discord.Embed(title=f"User Info - {member.name}", color=0xffa703)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="Username", value=member.name, inline=False)
        embed.add_field(name="Discriminator", value=member.discriminator, inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        
        # Handle if joined_at is None
        joined_at = member.joined_at.strftime("%Y-%m-%d %H:%M:%S") if member.joined_at else "Unknown"
        embed.add_field(name="Joined At", value=joined_at, inline=False)
        
        embed.add_field(name="Roles", value=", ".join([role.name for role in member.roles]), inline=False)
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

# Setup function
async def setup(client: commands.Bot):
    await client.add_cog(UserInfo(client))