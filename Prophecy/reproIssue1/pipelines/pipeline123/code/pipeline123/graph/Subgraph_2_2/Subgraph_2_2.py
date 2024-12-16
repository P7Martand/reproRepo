from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pipeline123.functions import *
from . import *
from .config import *

def Subgraph_2_2(spark: SparkSession, subgraph_config: SubgraphConfig) -> DataFrame:
    Config.update(subgraph_config)
    df_src_avro_CustsDatasetInput_2_2 = src_avro_CustsDatasetInput_2_2(spark)
    df_Subgraph_1_1_1_2_out0, df_Subgraph_1_1_1_2_target1 = Subgraph_1_1_1_2(
        spark, 
        subgraph_config.Subgraph_1_1_1_2, 
        df_src_avro_CustsDatasetInput_2_2, 
        df_src_avro_CustsDatasetInput_2_2
    )
    df_Subgraph_1_2_1_2_out0, df_Subgraph_1_2_1_2_target1 = Subgraph_1_2_1_2(
        spark, 
        subgraph_config.Subgraph_1_2_1_2, 
        df_Subgraph_1_1_1_2_out0, 
        df_Subgraph_1_1_1_2_target1
    )
    df_Subgraph_1_3_1_2_out0, df_Subgraph_1_3_1_2_target1 = Subgraph_1_3_1_2(
        spark, 
        subgraph_config.Subgraph_1_3_1_2, 
        df_src_avro_CustsDatasetInput_2_2
    )
    df_src_avro_CustsDatasetInput_1_1_2 = src_avro_CustsDatasetInput_1_1_2(spark)
    df_Subgraph_1_4_2_out0, df_Subgraph_1_4_2_target1 = Subgraph_1_4_2(
        spark, 
        subgraph_config.Subgraph_1_4_2, 
        df_src_avro_CustsDatasetInput_2_2
    )
    df_identity_transform_2_2 = identity_transform_2_2(spark, df_src_avro_CustsDatasetInput_2_2)
    df_identity_transform_1_1_2 = identity_transform_1_1_2(spark, df_src_avro_CustsDatasetInput_1_1_2)
    df_multi_join_1_2 = multi_join_1_2(
        spark, 
        df_Subgraph_1_3_1_2_target1, 
        df_Subgraph_1_4_2_target1, 
        df_Subgraph_1_1_1_2_target1, 
        df_Subgraph_1_2_1_2_target1, 
        df_Subgraph_1_1_1_2_target1
    )
    subgraph_config.update(Config)

    return df_multi_join_1_2
