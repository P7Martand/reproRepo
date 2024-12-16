from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pipeline123.functions import *
from . import *
from .config import *

def Subgraph_2_2_4(spark: SparkSession, subgraph_config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(subgraph_config)
    df_Limit_3_2 = Limit_3_2(spark, in0)
    df_Reformat_1_2 = Reformat_1_2(spark, in0)
    subgraph_config.update(Config)

    return df_Limit_3_2
