import bot
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('MY_TOKEN')

if __name__ == '__main__':
    #run the bot
    bot.run_discord_bot()
