from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("PrintFactSales").getOrCreate()
    df = spark.sql("SELECT * FROM source.fact_sales")
    df.show()

if __name__ == "__main__":
    main()
