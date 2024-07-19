import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import handle_response

# Load our token
load_dotenv()
token = os.getenv('MY_TOKEN')

# setting up intents / Bot config
intents = Intents.default()
intents.message_content = True 
client = Client(intents=intents)

# message functionality
async def send_message(message, user_message):
    if not user_message:
        print('Message was empty because intents were not enabled...probably')
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    try:
        response = handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# handling the startup
@client.event
async def on_ready():
    print(f'{client.user} is now running!')

# handling incoming messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[in channel "{channel}"] {username}:"{user_message}"')
    await send_message(message, user_message)

# main entry
def main():
    client.run(token)

if __name__ == '__main__':
    main()