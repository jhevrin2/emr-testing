import logging
import pandas as pd
from pyspark.sql import SparkSession

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_spark_session():
    logging.info("Setting up Spark Context")
    return SparkSession.builder \
        .master("yarn") \
        .appName("Test EMR") \
        .getOrCreate()


if __name__ == "__main__":
    spark = get_spark_session()
    logging.info("Reading and writing to S3")
    data = pd.read_csv("https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv")
    spark_df = spark.createDataFrame(data.select_dtypes(exclude=object))
    spark_df.sample(0.5).write.mode('overwrite').orc("s3a://jhevrin2-datasci/datascience/titanic/titanic-sample.orc")
