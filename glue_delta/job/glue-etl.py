
from pyspark.sql import SparkSession
from pyspark import SparkConf

# begin code 
if __name__ == '__main__': 
    
    spark = SparkSession \
        .builder \
        .appName("load_dfp_to_delta") \
        .getOrCreate()
    
    df = spark.read \
        .format("csv") \
        .option("inferSchema", "true") \
        .option("header", "true") \
        .option("delimiter", ";") \
        .csv("s3://de-okkus-landing-dev-727477891012/2024/01/17/dfp/dfp_cia_aberta_DRE_ind_2023.csv")
        
        
        
    df.write \
        .mode("overwrite") \
        .format("delta") \
        .save("s3://de-okkus-bronze-727477891012/2024/01/17/dfp/dfp_cia_aberta_DRE_ind_2023")