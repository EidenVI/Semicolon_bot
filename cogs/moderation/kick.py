import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class Kick(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # /Kick command
    @app_commands.command(name='kick', description="Kick a member from the server")
    @commands.has_guild_permissions(kick_members=True)
    @app_commands.describe(member='member to kick from the server', reason='reason for kicking the member')
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str] = 'no reason'):
        try:
            if not interaction.guild.me.guild_permissions.kick_members:
                await interaction.response.send_message("I don't have the necessary permission to kick members.", ephemeral=True)
                return
            if interaction.user == member:
                await interaction.response.send_message("You can't kick yourself!", ephemeral=True)
                return
            if member.guild_permissions.administrator:
                await interaction.response.send_message("You can't kick an administrator!", ephemeral=True)
                return

            await member.kick(reason=reason if reason != 'no reason' else None)
            await interaction.response.send_message(f"{member.name} was kicked by {interaction.user.mention}", ephemeral=True)
        except discord.errors.NotFound:
            await interaction.response.send_message("Member not found.", ephemeral=True)
        except discord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error kicking member: {e.status} {e.text}", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {e}", ephemeral=True)

# setup func
async def setup(client: commands.Bot) -> None:
    await client.add_cog(Kick(client))
