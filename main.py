from logic import discord_client, kafka_message_send
from os import getenv

TOKEN_DISCORD = getenv('TOKEN_DISCORD')
kafka_server = kafka_message_send.KafkaMessageSend('localhost', 9091, 'ponto')
client = discord_client.DiscordClient(kafka_server)
client.run(TOKEN_DISCORD)

