from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from pipeline123.functions import *

def identity_transform_1_1_1_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0
