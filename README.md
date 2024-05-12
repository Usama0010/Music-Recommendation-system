# Music-Recommendation-system
Spotify’s music recommendation system is powered by machine learning algorithms that analyse user behaviour, preferences, and listening habits to generate personalised recommendations. These algorithms consider factors such as the songs users listen to, how often they listen, playlists they create, and artists they follow.

Usama Bin Sajid 19i-1864
Syed Danish 22i-1860
Mujahid Abbas 22i-1969

PROJECT_REPORT:

App.py:
   **Introduction**
The provided app.py file contains the code for a Flask application that serves real-time music recommendations to users based on their activity. The application integrates with Kafka for consuming user activity data and MongoDB for retrieving music recommendations. Additionally, it utilizes Flask-SocketIO for real-time communication between the server and clients.

  •**Overview of Components**
Flask: Flask is a micro web framework written in Python used for developing web applications. It provides the basic tools and libraries needed for web development.
Flask-SocketIO: Flask-SocketIO is an extension for Flask that adds WebSocket support to applications. It enables real-time, bidirectional communication between the client and server.
Kafka: Apache Kafka is an open-source distributed event streaming platform used for building real-time data pipelines and streaming applications. In this application, Kafka is used for consuming user activity data.
MongoDB: MongoDB is a NoSQL database that stores data in flexible, JSON-like documents. It is used in this application to store music metadata and retrieve recommendations based on user activity.
    • **Functionality**
Flask Routes: The application defines a single route ("/") that renders the index.html template. This route serves as the main entry point for users accessing the application.
SocketIO Connection: Upon establishing a connection with the client, the server emits a "response" event to confirm the connection.
Kafka Consumer Thread: The application spawns a separate thread (kafka_consumer_thread) responsible for consuming messages from Kafka. Each message represents user activity, such as listening to a song or liking a track.
MongoDB Query: Within the Kafka consumer thread, the application queries MongoDB to retrieve music recommendations based on the user's activity. The query retrieves documents from the MongoDB collection based on specified criteria, such as genre and popularity.
Real-Time Updates: Upon receiving new recommendations from MongoDB, the server emits a "new_recommendations" event to the client using SocketIO. The client-side JavaScript can then update the user interface to display the latest recommendations.
    • **Code Walkthrough**
Imports: The necessary libraries and modules are imported, including Flask, Flask-SocketIO, threading, Kafka consumer, and MongoDB client.
Function Definitions: Two main functions are defined:
get_recommendations_from_mongodb(): Connects to MongoDB and retrieves music recommendations based on specified criteria.
kafka_consumer_thread(): Defines the Kafka consumer thread responsible for consuming user activity data and fetching recommendations.
Flask Routes and SocketIO Events: The Flask routes and SocketIO events are defined to handle client-server communication.
Main Execution: The main block of code starts the Kafka consumer thread and runs the Flask application using SocketIO.

**Consumer.py:**
    • **Introduction**
The consumer.py script is designed to consume messages from a Kafka topic named 'track_data'. It utilizes the KafkaConsumer class from the kafka-python library to establish a connection to a Kafka broker and consume messages in real-time. The script is intended to be part of a larger system where it processes incoming track data messages and performs further actions such as generating recommendations or executing other business logic.

    **Functionality Overview**
The consumer.py script performs the following main functions:

Create Consumer: Establishes a connection to the Kafka broker and creates a Kafka consumer object configured to consume messages from the 'track_data' topic.
Consume Messages: Iterates over messages received from the Kafka topic, extracts the track data payload, and processes it further as needed. In this script, it simply prints the received track data to the console.
    • Detailed Analysis
1. create_consumer() Function:
Purpose: This function creates a Kafka consumer object with the specified configuration.
Parameters:
None
Return Value:
consumer: KafkaConsumer object configured to consume messages from the 'track_data' topic.
Configuration Parameters:
bootstrap_servers: Specifies the list of Kafka broker addresses to bootstrap the connection.
auto_offset_reset: Determines the initial offset used when the consumer starts reading a partition with no committed offset. Here, it is set to 'earliest', indicating that the consumer starts reading from the earliest available message.
value_deserializer: Specifies a deserializer function to deserialize message values from bytes to Python objects. In this case, it uses a lambda function to deserialize JSON-encoded messages.
2. consume_messages(consumer) Function:
Purpose: This function consumes messages from the Kafka topic using the provided Kafka consumer object.
Parameters:
consumer: KafkaConsumer object created by create_consumer() function.
Processing:
Iterates over messages received from the Kafka topic.
Extracts the value (track data) from each message.
Prints the received track data to the console.
Further processing logic, such as generating recommendations, can be added here.
    • Execution
The script can be executed standalone by running it directly. Upon execution, it establishes a connection to the Kafka broker, consumes messages from the 'track_data' topic, and prints the received track data to the console in real-time.

Producer.py:

    •  Introduction
The producer.py script is designed to fetch data from a MongoDB database and stream it to a Kafka topic in real-time. It utilizes the Kafka and pymongo libraries to achieve this functionality. The primary goal is to facilitate the ingestion of data from a MongoDB collection into a Kafka topic for further processing or analysis.

    •  Functionality Overview
 create_producer() Function
This function creates a KafkaProducer instance with the specified bootstrap servers and a custom value serializer for JSON data.
The KafkaProducer instance is returned to be used for sending data to Kafka topics. fetch_data_from_mongodb() Function
This function establishes a connection to a local MongoDB instance and retrieves data from a specified collection (features1 in this case).
It uses a generator to continuously yield JSON-serialized documents from the MongoDB collection.
    • send_data() Function:
This function takes a KafkaProducer instance and a topic name as input parameters.
It iterates over the data fetched from MongoDB using the fetch_data_from_mongodb() generator.
For each document retrieved, it sends the data to the specified Kafka topic using the KafkaProducer instance.
The flush() method ensures that the data is immediately sent to Kafka, and the time.sleep(1) simulates real-time data streaming by introducing a 1-second delay between each data transmission.
    • Execution Flow
The create_producer() function is called to initialize a KafkaProducer instance.
The send_data() function is invoked with the KafkaProducer instance and the target Kafka topic name (track_data).
Inside the send_data() function, data is continuously fetched from MongoDB using the fetch_data_from_mongodb() generator.
Each document retrieved from MongoDB is serialized to JSON and sent to the Kafka topic using the KafkaProducer instance.
The process repeats indefinitely, ensuring continuous real-time data streaming from MongoDB to Kafka.

Your_Script.py:
    • Introduction
In this project, we explore the use of Locality Sensitive Hashing (LSH) for music recommendation. LSH is a technique used for approximate nearest neighbor search, which is particularly useful in large-scale recommendation systems. By hashing similar data points to the same bucket, LSH enables efficient retrieval of similar items from a large dataset.
    • Script Overview
The provided Python script leverages PySpark to implement LSH for music recommendation. Below is a breakdown of the script's functionality:
Initialization: The script initializes a SparkSession, configuring it to read and write data from MongoDB.
Data Loading: Data is loaded from MongoDB into a Spark DataFrame. The schema of the DataFrame is printed to understand the structure of the data.
Feature Transformation: A user-defined function (UDF) is defined to convert an array of doubles into a Dense Vector, which is a requirement for LSH. This function is applied to create a new column named 'features_vec' in the DataFrame.
LSH Model Definition: The BucketedRandomProjectionLSH model is defined with specified parameters such as input and output columns, bucket length, and number of hash tables.
Model Fitting: The LSH model is fitted to the DataFrame containing the transformed features.
Transformations: The fitted model is used to transform the feature DataFrame, adding a new column named 'hashes' containing the hash keys.
Approximate Nearest Neighbors Search: An example is provided to find approximate nearest neighbors for the first 5 features in the dataset. The model's approxNearestNeighbors method is used to perform the search.
    • Results and Discussion
The script successfully demonstrates the implementation of LSH for music recommendation using PySpark. Key points to note include:
Efficient storage and retrieval of high-dimensional feature vectors using LSH.
Scalability of LSH for handling large datasets.
Approximate nearest neighbor search provides fast and effective recommendations.

Index.html:
    • Introduction
The provided index.html file presents a prototype for a simple interactive music streaming service. The prototype includes functionality to display recommendations dynamically as they are received from the server using WebSocket technology.

    • Overview of the HTML Structure
The HTML structure consists of standard HTML5 elements, including <html>, <head>, and <body>. Key components of the HTML file include:
Title: The title of the webpage is set to "Music Streaming Service" to provide context to the user.
Script Tags: JavaScript code is embedded within <script> tags to handle client-side interactions and dynamically update recommendations.

    •  Script Functionality
The JavaScript code included within the <script> tags is responsible for establishing a WebSocket connection with the server and handling incoming recommendation data. Here's an overview of the script functionality:
Event Listener: The DOMContentLoaded event listener ensures that the JavaScript code executes after the DOM content has been fully loaded.
Socket Connection: The io.connect() method establishes a WebSocket connection with the server. The server URL is dynamically constructed based on the protocol, domain, and port of the current location.
Event Handling: The socket.on() method listens for the 'new_recommendations' event emitted by the server. When new recommendations are received, the corresponding callback function is executed.
Updating Recommendations: Upon receiving new recommendations, the callback function clears the existing recommendations list and populates it with the latest recommendations received from the server.

Project.ipynb:
    • Introduction
The project aims to extract audio features from a collection of music tracks stored as MP3 files and store these features, along with corresponding metadata, in a MongoDB database. Audio feature extraction is a crucial step in music information retrieval, enabling tasks such as genre classification, music recommendation, and similarity analysis.

    • Implementation Details
Data Loading and Cleaning
The project begins by loading a CSV file containing metadata about music tracks, including track ID, title, genre, tags, listens, date created, type, and name.
The load_and_clean_data function is used to load the CSV file into a Pandas DataFrame and perform data cleaning operations.
Duplicate rows are removed based on specific columns to ensure data integrity.
Only selected columns, including track ID, title, genre, tags, listens, date created, type, and name, are retained for further processing.
    • Feature Extraction
Audio features are extracted from MP3 files using the Librosa library, which provides tools for audio and music analysis.
The extract_features function computes three main features: MFCC (Mel-Frequency Cepstral Coefficients), Spectral Centroid, and Zero-Crossing Rate.
MFCC represents the spectral envelope of an audio signal, while Spectral Centroid indicates the "center of mass" of the audio spectrum. Zero-Crossing Rate measures the rate at which the audio signal changes its sign.
These features are extracted for each MP3 file in the specified directory.
    • MongoDB Integration
A MongoDB database is used to store the extracted audio features along with corresponding metadata.
The process_files function iterates through the MP3 files in the specified directory, extracts features for each file, and stores them in the MongoDB database.
Metadata such as track ID, title, genre, tags, listens, date created, type, and name are retrieved from the DataFrame and stored alongside the extracted features.
Each document in the MongoDB collection represents a music track and contains both metadata and extracted features.
    • Results and Discussion
The project successfully extracts audio features from MP3 files and stores them in a MongoDB database.
By combining metadata with audio features, the database provides a comprehensive representation of music tracks, facilitating further analysis and exploration.
The use of MongoDB enables efficient storage and retrieval of large volumes of audio data, supporting scalable applications in music research and recommendation systems.


