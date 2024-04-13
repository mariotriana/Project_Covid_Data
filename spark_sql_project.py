
import argparse
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

parser = argparse.ArgumentParser()

parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)

args = parser.parse_args()

input = args.input
output = args.output

spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()
    
df = spark.read.parquet(input)

df = df.withColumn('Date_reported', F.to_timestamp(F.col('Date_reported'), 'yyyy-MM-dd'))\
    .withColumn('New_cases', F.col('New_cases').cast('Integer'))\
    .withColumn('Cumulative_cases', F.col('Cumulative_cases').cast('Integer'))\
    .withColumn('New_deaths', F.col('New_deaths').cast('Integer'))\
    .withColumn('Cumulative_deaths', F.col('Cumulative_deaths').cast('Integer'))

df.registerTempTable('covid_data')

df_result = spark.sql("""
SELECT
    Country,Date_reported,
    SUM (Cumulative_cases) AS total_country_cases,
    AVG (Cumulative_cases) AS average_cases,
    SUM (Cumulative_cases) AS total_country_deaths,
    AVG (Cumulative_deaths) AS average_deaths
FROM
    covid_data
GROUP BY 1,2
ORDER BY Date_reported DESC
""")

output = "gs://covid-data-project-bucket/output-data"
df_result.coalesce(1).write.parquet(output, mode='overwrite')

