import json
from kafka import KafkaProducer


class KafkaMessageSend:
    def __init__(self, server, port, topic):
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=[f'{server}:{port}'])

    def send_message(self, message):
        self.producer.send(self.topic, json.dumps(message).encode('utf-8'))
        self.producer.flush()