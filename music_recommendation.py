from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vectors, VectorUDT
from pyspark.ml.feature import BucketedRandomProjectionLSH

def main():
    spark = SparkSession.builder \
        .appName("Music Recommendation with LSH") \
        .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/audio_features_db1.features1") \
        .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/audio_features_db1.features1") \
        .getOrCreate()

    # Load data
    df = spark.read.format("mongo").load()

    # Print the schema to understand how data is structured
    df.printSchema()

    # UDF to convert array of doubles into a Dense Vector
    array_to_vector = udf(lambda x: Vectors.dense(x), VectorUDT())

    # Apply UDF to create new column 'features_vec'
    df = df.withColumn("features_vec", array_to_vector(df["features.mfcc"]))

    # Define LSH model
    brp = BucketedRandomProjectionLSH(inputCol="features_vec", outputCol="hashes", bucketLength=2.0, numHashTables=3)
    model = brp.fit(df)

    # Transform the feature dataframe to include hash keys
    transformed_df = model.transform(df)

    # Show the schema to see the hashes
    transformed_df.printSchema()

    # Example: Find approx nearest neighbors for the first 5 features
    print("Approximately searching for 5 nearest neighbors:")
    for row in df.head(5):
        key = row['features_vec']
        neighbors = model.approxNearestNeighbors(df, key, 5)
        neighbors.show()

    spark.stop()

if __name__ == "__main__":
    main()

