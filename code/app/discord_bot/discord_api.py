from dotenv import load_dotenv
import discord
import os
from app.open_ai.openai import chatgpt_response

#Load environment variables
load_dotenv()

#Save discord token to variable
discord_token = os.getenv('DISCORD_TOKEN')


#Create a class called my client that can prep the Discord bot to take a message and what to do when it receives a message
class MyClient(discord.Client):
    async def on_ready(self):
        print('Successfully logged in as: ', self.user)
        
    async def on_message(self, message):
        print(message.content)
        #Prevents bot from responding to itself
        if message.author == self.user:
            return
        command, user_message = None, None
        
        #Parses message text that contains certain commands.
        for text in ['/ai', '/bot', '/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)
        
        #Sends prompt to openai api retrieval to get answer if command is correct
        if command == '/ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt = user_message)
            await message.channel.send(f'Answer: {bot_response}')
            

#Sends message content to discord bot to repeat to user            
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents = intents)