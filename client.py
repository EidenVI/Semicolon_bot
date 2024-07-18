import os
import discord
from discord.ext import commands
from discord import app_commands
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(';'), intents=discord.Intents.all(), application_id=os.getenv('DISCORD_APPLICATION_ID'))
        self.cogs_list = ['moderation', 'general', 'fun', 'server_setup']

    async def setup_hook(self):
        for folder in self.cogs_list:
            for filename in os.listdir(f'cogs/{folder}'):
                if filename.endswith('.py'):
                    try:
                        await self.load_extension(f'cogs.{folder}.{filename[:-3]}')
                    except commands.errors.ExtensionAlreadyLoaded:
                        pass  # Ignore if the extension is already loaded
                    except Exception as e:
                        print(f"Failed to load extension cogs.{folder}.{filename[:-3]}: {e}")

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.setup_hook()
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(f"Failed to sync commands: {e}")
        print('--------------')