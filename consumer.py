# consumer.py
from kafka import KafkaConsumer
import json

def create_consumer():
    consumer = KafkaConsumer('track_data',
                             bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    return consumer

def consume_messages(consumer):
    for message in consumer:
        track_data = message.value
        print(f"Received track data: {track_data}")
        # Handle recommendations or other logic here

if __name__ == "__main__":
    consumer = create_consumer()
    consume_messages(consumer)
