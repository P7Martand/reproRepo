from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline123.config.ConfigStore import *
from pipeline123.functions import *

def multi_join(
        spark: SparkSession,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame, 
        in3: DataFrame, 
        in4: DataFrame
) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), lit(True), "inner")\
        .join(in2.alias("in2"), lit(True), "inner")\
        .join(in3.alias("in3"), lit(True), "inner")\
        .join(in4.alias("in4"), lit(True), "inner")\
        .select(col("in0.customer_id").alias("customer_id"), col("in0.first_name").alias("first_name"), col("in1.last_name").alias("last_name"), col("in1.phone").alias("phone"), col("in2.email").alias("email"), col("in2.country_code").alias("country_code"), col("in3.account_open_date").alias("account_open_date"), col("in4.account_flags").alias("account_flags"))
