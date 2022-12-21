from datetime import datetime
from typing import Any
from logic.kafka_message_send import KafkaMessageSend
import discord


class DiscordClient(discord.Client):

    def __init__(self, kafka_server: KafkaMessageSend, **options: Any) -> None:
        intents = discord.Intents().default()
        intents.message_content = True
        intents.guild_messages = True
        intents.voice_states = True
        intents.members = True
        super().__init__(intents= intents, **options)
        self._kafka_server = kafka_server

    async def on_voice_state_update(self, member, before, after):
        if before.channel or after.channel:
            message = {'time': str(datetime.now())}
            if after.channel:
                message['channel'] = after.channel.name
                message['status'] = True
            else:
                message['channel'] = before.channel.name
                message['status'] = False

            self._kafka_server.send_message(message)


