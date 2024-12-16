from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline123.config.ConfigStore import *
from pipeline123.functions import *

def src_avro_CustsDatasetInput(spark: SparkSession) -> DataFrame:
    return spark.read.format("avro").load("dbfs:/Prophecy/qa_data/avro/CustomersDatasetInput.avro")
