from logic import discord_client, kafka_message_send

kafka_server = kafka_message_send.KafkaMessageSend('localhost', 9091, 'ponto')
client = discord_client.DiscordClient(kafka_server)
client.run('MTA1NDM4MTg4MzMxMzYyNzE1Ng.GejgPA.MKrY3kipHOutYCcCYxZ0G3XMH4P4tXkg393R28')

