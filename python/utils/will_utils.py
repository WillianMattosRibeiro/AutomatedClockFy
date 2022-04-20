def init_spark(job_name=None):
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.getOrCreate()
    return spark

def get_json(spark, path):
    df = spark.read.json(path).collect()
    df_list_of_dict = [row.asDict() for row in df.collect()]
    return df_list_of_dict
