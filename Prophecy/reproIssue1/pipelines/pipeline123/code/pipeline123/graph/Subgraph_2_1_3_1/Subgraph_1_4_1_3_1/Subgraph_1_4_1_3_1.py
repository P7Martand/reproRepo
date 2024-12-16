from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pipeline123.functions import *
from . import *
from .config import *

def Subgraph_1_4_1_3_1(spark: SparkSession, subgraph_config: SubgraphConfig, in1: DataFrame) -> (DataFrame, DataFrame):
    Config.update(subgraph_config)
    df_Subgraph_2_4 = Subgraph_2_4(spark, subgraph_config.Subgraph_2_4, in1)
    df_Limit_2 = Limit_2(spark, in1)
    df_Limit_1 = Limit_1(spark, in1)
    df_Filter_1 = Filter_1(spark, in1)
    subgraph_config.update(Config)

    return df_Filter_1, df_Subgraph_2_4
