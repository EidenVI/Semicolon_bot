import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class Ban(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # /Ban command 
    @app_commands.command(name='ban', description="Ban a member from the server")
    @commands.has_guild_permissions(ban_members=True)
    @app_commands.describe(member='Member to ban from the server', reason='Reason for banning the member')
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str] = 'no reason'):
        try:
            if not interaction.guild.me.guild_permissions.ban_members:
                await interaction.response.send_message("I don't have the necessary permission to ban members.", ephemeral=True)
                return
            if interaction.user == member:
                await interaction.response.send_message("You can't ban yourself!", ephemeral=True)
                return
            if member.guild_permissions.administrator:
                await interaction.response.send_message("You can't ban an administrator!", ephemeral=True)
                return

            await member.ban(reason=reason if reason!= 'no reason' else None)
            await interaction.response.send_message(f"{member.name} was banned by {interaction.user.mention}", ephemeral=True)
        except discord.errors.NotFound:
            await interaction.response.send_message("Member not found.", ephemeral=True)
        except discord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error banning member: {e.status} {e.text}", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {e}", ephemeral=True)


class BanContext(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    async def setup(self, client: commands.Bot) -> None:
        @client.tree.context_menu(name='Ban member')
        @commands.has_guild_permissions(ban_members=True)
        async def ban_context_menu(interaction: discord.Interaction, member: discord.Member) -> None:
            try:
                if not interaction.guild.me.guild_permissions.ban_members:
                    await interaction.response.send_message("I don't have the necessary permission to ban members.", ephemeral=True)
                    return
                if interaction.user == member:
                    await interaction.response.send_message("You can't ban yourself!", ephemeral=True)
                    return
                if member.guild_permissions.administrator:
                    await interaction.response.send_message("You can't ban an administrator!", ephemeral=True)
                    return

                await member.ban(reason=f"Banned by {interaction.user.mention}")
                await interaction.response.send_message(f"{member.name} was banned by {interaction.user.mention}", ephemeral=True)
            except discord.errors.NotFound:
                await interaction.response.send_message("Member not found.", ephemeral=True)
            except discord.errors.HTTPException as e:
                await interaction.response.send_message(f"Error banning member: {e.status} {e.text}", ephemeral=True)
            except Exception as e:
                await interaction.response.send_message(f"An unexpected error occurred: {e}", ephemeral=True)

        await client.add_cog(self)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Ban(client))
    await client.add_cog(BanContext(client))