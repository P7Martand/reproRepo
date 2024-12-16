from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pipeline123.functions import *
from . import *
from .config import *

def Subgraph_1_2_1_1_1_1(
        spark: SparkSession,
        subgraph_config: SubgraphConfig,
        in0: DataFrame,
        source1: DataFrame
) -> (DataFrame, DataFrame):
    Config.update(subgraph_config)
    df_Limit_1_2 = Limit_1_2(spark, in0)
    df_Filter_1_2 = Filter_1_2(spark, in0)
    df_Subgraph_2_2_4 = Subgraph_2_2_4(spark, subgraph_config.Subgraph_2_2_4, source1)
    df_Limit_2_2 = Limit_2_2(spark, source1)
    subgraph_config.update(Config)

    return df_Filter_1_2, df_Limit_2_2
