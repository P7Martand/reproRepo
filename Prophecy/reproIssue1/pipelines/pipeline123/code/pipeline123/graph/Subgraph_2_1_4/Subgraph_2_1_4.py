from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pipeline123.functions import *
from . import *
from .config import *

def Subgraph_2_1_4(spark: SparkSession, subgraph_config: SubgraphConfig, source0: DataFrame) -> DataFrame:
    Config.update(subgraph_config)
    df_src_avro_CustsDatasetInput_1_1_1_4 = src_avro_CustsDatasetInput_1_1_1_4(spark)
    df_src_avro_CustsDatasetInput_2_1_4 = src_avro_CustsDatasetInput_2_1_4(spark)
    df_Subgraph_1_3_1_1_4_out0, df_Subgraph_1_3_1_1_4_target1 = Subgraph_1_3_1_1_4(
        spark, 
        subgraph_config.Subgraph_1_3_1_1_4, 
        df_src_avro_CustsDatasetInput_2_1_4
    )
    df_Subgraph_1_4_1_4_out0, df_Subgraph_1_4_1_4_target1 = Subgraph_1_4_1_4(
        spark, 
        subgraph_config.Subgraph_1_4_1_4, 
        df_src_avro_CustsDatasetInput_2_1_4
    )
    df_Subgraph_1_1_1_1_4_out0, df_Subgraph_1_1_1_1_4_target1 = Subgraph_1_1_1_1_4(
        spark, 
        subgraph_config.Subgraph_1_1_1_1_4, 
        df_src_avro_CustsDatasetInput_2_1_4, 
        df_src_avro_CustsDatasetInput_2_1_4
    )
    df_Subgraph_1_2_1_1_4_out0, df_Subgraph_1_2_1_1_4_target1 = Subgraph_1_2_1_1_4(
        spark, 
        subgraph_config.Subgraph_1_2_1_1_4, 
        df_Subgraph_1_1_1_1_4_out0, 
        df_Subgraph_1_1_1_1_4_target1
    )
    df_multi_join_1_1_4 = multi_join_1_1_4(
        spark, 
        df_Subgraph_1_3_1_1_4_target1, 
        df_Subgraph_1_4_1_4_target1, 
        df_Subgraph_1_1_1_1_4_target1, 
        df_Subgraph_1_2_1_1_4_target1, 
        df_Subgraph_1_1_1_1_4_target1
    )
    df_identity_transform_2_1_4 = identity_transform_2_1_4(spark, df_src_avro_CustsDatasetInput_2_1_4)
    df_identity_transform_1_1_1_4 = identity_transform_1_1_1_4(spark, df_src_avro_CustsDatasetInput_1_1_1_4)
    subgraph_config.update(Config)

    return df_multi_join_1_1_4
