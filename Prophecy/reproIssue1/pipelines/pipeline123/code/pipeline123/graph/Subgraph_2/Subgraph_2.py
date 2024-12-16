from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pipeline123.functions import *
from . import *
from .config import *

def Subgraph_2(spark: SparkSession, subgraph_config: SubgraphConfig, source0: DataFrame) -> DataFrame:
    Config.update(subgraph_config)
    df_src_avro_CustsDatasetInput_2 = src_avro_CustsDatasetInput_2(spark)
    df_Subgraph_1_3_1_out0, df_Subgraph_1_3_1_target1 = Subgraph_1_3_1(
        spark, 
        subgraph_config.Subgraph_1_3_1, 
        df_src_avro_CustsDatasetInput_2
    )
    df_Subgraph_1_4_out0, df_Subgraph_1_4_target1 = Subgraph_1_4(
        spark, 
        subgraph_config.Subgraph_1_4, 
        df_src_avro_CustsDatasetInput_2
    )
    df_Subgraph_1_1_1_out0, df_Subgraph_1_1_1_target1 = Subgraph_1_1_1(
        spark, 
        subgraph_config.Subgraph_1_1_1, 
        df_src_avro_CustsDatasetInput_2, 
        df_src_avro_CustsDatasetInput_2
    )
    df_Subgraph_1_2_1_out0, df_Subgraph_1_2_1_target1 = Subgraph_1_2_1(
        spark, 
        subgraph_config.Subgraph_1_2_1, 
        df_Subgraph_1_1_1_out0, 
        df_Subgraph_1_1_1_target1
    )
    df_multi_join_1 = multi_join_1(
        spark, 
        df_Subgraph_1_3_1_target1, 
        df_Subgraph_1_4_target1, 
        df_Subgraph_1_1_1_target1, 
        df_Subgraph_1_2_1_target1, 
        df_Subgraph_1_1_1_target1
    )
    df_src_avro_CustsDatasetInput_1_1 = src_avro_CustsDatasetInput_1_1(spark)
    df_identity_transform_1_1 = identity_transform_1_1(spark, df_src_avro_CustsDatasetInput_1_1)
    df_identity_transform_2 = identity_transform_2(spark, df_src_avro_CustsDatasetInput_2)
    subgraph_config.update(Config)

    return df_multi_join_1
