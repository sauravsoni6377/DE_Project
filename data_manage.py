from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from sqlalchemy import create_engine

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("IndiaTourismDataProcessor") \
    .getOrCreate()

# Load the dataset using Spark
file_path = 'india_tourist_analysis.csv'
df = spark.read.option("header", "true").csv(file_path)

# Clean and preprocess the data
df = df.fillna(0)  # Replace NaN with 0
df = df.withColumnRenamed("Circle", "circle") \
       .withColumnRenamed("Name of the Monument ", "monument_name") \
       .withColumnRenamed("Domestic-2019-20", "domestic_2019_20") \
       .withColumnRenamed("Foreign-2019-20", "foreign_2019_20") \
       .withColumnRenamed("Domestic-2020-21", "domestic_2020_21") \
       .withColumnRenamed("Foreign-2020-21", "foreign_2020_21") \
       .withColumnRenamed("% Growth 2021-21/2019-20-Domestic", "growth_domestic") \
       .withColumnRenamed("% Growth 2021-21/2019-20-Foreign", "growth_foreign")

# Convert data types (if necessary)
df = df.withColumn("domestic_2019_20", col("domestic_2019_20").cast("float")) \
       .withColumn("foreign_2019_20", col("foreign_2019_20").cast("float")) \
       .withColumn("domestic_2020_21", col("domestic_2020_21").cast("float")) \
       .withColumn("foreign_2020_21", col("foreign_2020_21").cast("float")) \
       .withColumn("growth_domestic", col("growth_domestic").cast("float")) \
       .withColumn("growth_foreign", col("growth_foreign").cast("float"))

# Convert Spark DataFrame to Pandas DataFrame for MySQL upload
data = df.toPandas()

# Save data to MySQL
db_config = {
    'user': 'root',
    'password': 'sanj6132',
    'host': 'localhost',
    'port': 3306,
    'database': 'tourism_db'
}
engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

data.to_sql('tourism_data', con=engine, index=False, if_exists='replace')
print("Data successfully processed with Spark and transferred to MySQL!")
