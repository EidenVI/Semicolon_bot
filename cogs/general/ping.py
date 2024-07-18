import discord
from discord import app_commands
from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='ping', description='Latency? What latency?')
    async def ping(self, interaction: discord.Interaction):
        latency = self.client.latency * 1000

        embed = discord.Embed(
            title='🏓 Pong!',
            description=f'Latency: `{latency:.2f}ms`',
            color=discord.Color.green()
        )
        embed.set_thumbnail(url='https://example.com/ping_image.png')
        embed.set_footer(text='Ping Command', icon_url=interaction.user.avatar.url)
        embed.timestamp = discord.utils.utcnow()

        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(client):
    await client.add_cog(PingCommand(client))
