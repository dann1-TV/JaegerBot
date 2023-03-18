import discord
from datetime import datetime

import responses
import tarkov

# TODO: Use kwargs
async def send_message(message, user_message, is_private, tarkov_data):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot(auth_token):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    tarkov_data = {}
    tarkov_data['maps'] = tarkov.load_maps
    tarkov_data['tips'] = tarkov.load_tips 
        
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        log_bot(username, user_message, channel)

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, True, tarkov_data)
        if user_message[0] == '!':
            await send_message(message, user_message, False, tarkov_data)

    client.run(auth_token)


def log_bot(username, user_message, channel):
    file = open('JaegerBot.log', 'a')

    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")

    file.write(f'{date}: {username}> typed: "{user_message}" at #{channel}\n')

    file.close()
