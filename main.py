import asyncio
import os
from dotenv import load_dotenv
from client import Client

load_dotenv()

async def main():
    async with Client() as client:
        await client.start(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    asyncio.run(main())
