# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
from consumer import create_consumer
from pymongo import MongoClient
import json

app = Flask(__name__)
socketio = SocketIO(app)

# Function to connect to MongoDB and retrieve recommendations based on track metadata
def get_recommendations_from_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['audio_features_db1']  # Replace 'your_database_name' with your actual database name
    collection = db['features1']  # Replace 'your_collection_name' with the name of your collection
    # Example query: Retrieve documents where 'genre_top' is 'Rock', ordered by 'listens' descending
    recommendations = list(collection.find({'genre_top': 'Pop'}).sort('listens', -1).limit(10))
    #recommendations = list(collection.find({'name': 'AWOL'}).sort('listens', -1).limit(10))
    # Convert ObjectId to string for serialization
    for recommendation in recommendations:
        recommendation['_id'] = str(recommendation['_id'])
    return recommendations

def kafka_consumer_thread():
    consumer = create_consumer()
    for message in consumer:
        user_activity = message.value
        recommendations = get_recommendations_from_mongodb()
        socketio.emit('new_recommendations', {'recommendations': recommendations}, namespace='/stream')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/stream')
def test_connect():
    emit('response', {'data': 'Connected'})

if __name__ == "__main__":
    thread = threading.Thread(target=kafka_consumer_thread)
    thread.daemon = True
    thread.start()
    socketio.run(app, debug=True)
