# producer.py
from kafka import KafkaProducer
from pymongo import MongoClient
import json
import time

def create_producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    return producer

def fetch_data_from_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['audio_features_db1']
    collection = db['features1']

    while True:
        for track in collection.find():
            yield json.dumps(track, default=str)  # Ensure datetime and other objects are serialized properly

def send_data(producer, topic):
    for data in fetch_data_from_mongodb():
        producer.send(topic, data)
        producer.flush()
        time.sleep(1)  # Simulating real-time data streaming with a delay

if __name__ == "__main__":
    producer = create_producer()
    send_data(producer, 'track_data')
# producer.py
from kafka import KafkaProducer
from pymongo import MongoClient
import json
import time

def create_producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    return producer

def fetch_data_from_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['audio_features_db1']
    collection = db['features1']

    while True:
        for track in collection.find():
            yield json.dumps(track, default=str)  # Ensure datetime and other objects are serialized properly

def send_data(producer, topic):
    for data in fetch_data_from_mongodb():
        producer.send(topic, data)
        producer.flush()
        time.sleep(1)  # Simulating real-time data streaming with a delay

if __name__ == "__main__":
    producer = create_producer()
    send_data(producer, 'track_data')
# producer.py
from kafka import KafkaProducer
from pymongo import MongoClient
import json
import time

def create_producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    return producer

def fetch_data_from_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['audio_features_db1']
    collection = db['features1']

    while True:
        for track in collection.find():
            yield json.dumps(track, default=str)  # Ensure datetime and other objects are serialized properly

def send_data(producer, topic):
    for data in fetch_data_from_mongodb():
        producer.send(topic, data)
        producer.flush()
        time.sleep(1)  # Simulating real-time data streaming with a delay

if __name__ == "__main__":
    producer = create_producer()
    send_data(producer, 'track_data')
# producer.py
from kafka import KafkaProducer
from pymongo import MongoClient
import json
import time

def create_producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    return producer

def fetch_data_from_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['audio_features_db1']
    collection = db['features1']

    while True:
        for track in collection.find():
            yield json.dumps(track, default=str)  # Ensure datetime and other objects are serialized properly

def send_data(producer, topic):
    for data in fetch_data_from_mongodb():
        producer.send(topic, data)
        producer.flush()
        time.sleep(1)  # Simulating real-time data streaming with a delay

if __name__ == "__main__":
    producer = create_producer()
    send_data(producer, 'track_data')
