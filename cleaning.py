
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType,BooleanType,DateType,IntegerType,FloatType

spark = SparkSession.builder.appName("PF").config("spark.sql.caseSensitive", "True").getOrCreate()
df = spark.read.option("header",True) \
     .csv("./data/output/Master Ledger.xlsx - Master_Ledger.csv")
df = df.withColumn("ID",col("ID").cast(IntegerType()))\
        .withColumn("Amount",col("Amount").cast(FloatType()))\
        .withColumn("Subscriptions",col("Subscriptions").cast(BooleanType()))\
        .withColumn("Return",col("Return").cast(BooleanType()))
df = df.withColumn("Date",to_date(col("Date"),"MM/dd/yyyy"))
df.printSchema()

df.orderBy("ID", ascending=False).show()
df2 = spark.read.options(inferSchema='True',header='True').csv("C:/Users/Phan/Downloads/Github/personal-finance/data")
df2.show()