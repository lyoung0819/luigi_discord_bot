

# # sending messages
# async def send_message(message, user_message, is_private):
#     if not user_message:
#         print('Message was empty because intents were not enabled...probably')
#         return
#     # if message begins with '?', is_private=True and send privately
#     if is_private := user_message[0] == '?':
#         user_message = user_message[1:]
#     try:
#         response = handle_response(user_message)
#         await message.author.send(response) if is_private else await message.channel.send(response)
#     except Exception as e:
#         print(e)

# #running bot
# def run_discord_bot():
#     client = discord.Client(intents=discord.Intents.default())

#     @client.event
#     async def on_ready() -> None:
#         print(f"{client.user} is now running!")
#         return "Hello - It\'sa Luigi here! If you want to send a private mesage, begin your text with '?'"

#     @client.event
#     async def on_message(message):
#         # making sure you don't have an endless loop - ensuring the author of the message is not the bot, but the end user
#         if message.author == client.user:
#             return 
        
#         username = str(message.author)
#         user_message = message.content
#         channel = str(message.channel)
#         print(type(user_message))
#         print (f"{username} said: '{user_message}' in Channel:{channel}")

       

#     client.run(token)