from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from pipeline123.functions import *

def src_avro_CustsDatasetInput_2_1_2_1(spark: SparkSession) -> DataFrame:
    return spark.read.format("avro").load("dbfs:/Prophecy/qa_data/avro/CustomersDatasetInput.avro")
