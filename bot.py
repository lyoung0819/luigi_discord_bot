import discord
import responses
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('MY_TOKEN')


async def send_message(message, user_message, is_private):
    try:
        response = response.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    client.run(token)