import pandas as pd
from pyspark.sql import SparkSession


def get_spark_session():
    return SparkSession.builder \
        .master("yarn") \
        .appName("Test EMR") \
        .getOrCreate()


if __name__ == "__main__":
    spark = get_spark_session()
    data = pd.read_csv("https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv")
    spark_df = spark.createDataFrame(data.select_dtypes(exclude=object))
    spark_df.sample(0.5).write.orc("s3://jhevrin2-datasci/datascience/titanic/titanic-sample.orc")
