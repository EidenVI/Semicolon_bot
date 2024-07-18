import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class Unban(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        
    # /Unban command
    @app_commands.command(name='unban', description="Unban a member")
    @commands.has_guild_permissions(ban_members=True)
    @app_commands.describe(user="User to unban from the server", reason="Reason for unbanning the user")
    async def unban(self, interaction: discord.Interaction, user: discord.User, reason: Optional[str] = 'no reason'):
        try:
            if not interaction.guild.me.guild_permissions.ban_members:
                await interaction.response.send_message("I don't have the necessary permission to unban members.", ephemeral=True)
                return

            await interaction.guild.unban(user=user, reason=reason if reason != 'no reason' else None)
            await interaction.response.send_message(f"{user.name} was unbanned by {interaction.user.mention}", ephemeral=True)
        except discord.errors.NotFound:
            await interaction.response.send_message("User not found.", ephemeral=True)
        except discord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error unbanning user: {e.status} {e.text}", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {e}", ephemeral=True)

# setup func
async def setup(client: commands.Bot) -> None:
    await client.add_cog(Unban(client))
