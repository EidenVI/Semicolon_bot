import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class Mute(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # /Mute command
    @app_commands.command(name='mute', description="Mute a member in the server")
    @commands.has_guild_permissions(moderate_members=True)
    @app_commands.describe(member='member to mute', duration='duration of the mute in minutes', reason='reason for muting the member')
    async def mute(self, interaction: discord.Interaction, member: discord.Member, duration: int, reason: Optional[str] = 'no reason'):
        try:
            if not interaction.guild.me.guild_permissions.moderate_members:
                await interaction.response.send_message("I don't have the necessary permission to mute members.", ephemeral=True)
                return
            if interaction.user == member:
                await interaction.response.send_message("You can't mute yourself!", ephemeral=True)
                return
            if member.guild_permissions.administrator:
                await interaction.response.send_message("You can't mute an administrator!", ephemeral=True)
                return

            await member.timeout(duration=duration*60, reason=reason if reason != 'no reason' else None)
            await interaction.response.send_message(f"{member.name} was muted by {interaction.user.mention} for {duration} minutes", ephemeral=True)
        except discord.errors.NotFound:
            await interaction.response.send_message("Member not found.", ephemeral=True)
        except discord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error muting member: {e.status} {e.text}", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {e}", ephemeral=True)

# setup func
async def setup(client: commands.Bot) -> None:
    await client.add_cog(Mute(client))