from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline123.config.ConfigStore import *
from pipeline123.functions import *
from prophecy.utils import *
from pipeline123.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Subgraph_2 = Subgraph_2(spark, Config.Subgraph_2)
    df_Subgraph_2_1 = Subgraph_2_1(spark, Config.Subgraph_2_1, df_Subgraph_2)
    df_Subgraph_2_1_1 = Subgraph_2_1_1(spark, Config.Subgraph_2_1_1, df_Subgraph_2_1)
    df_src_avro_CustsDatasetInput = src_avro_CustsDatasetInput(spark)
    df_identity_transform = identity_transform(spark, df_src_avro_CustsDatasetInput)
    df_TRANSORMERS_1 = TRANSORMERS_1(spark, df_identity_transform)
    df_Subgraph_1_1_out0, df_Subgraph_1_1_target1 = Subgraph_1_1(
        spark, 
        Config.Subgraph_1_1, 
        df_src_avro_CustsDatasetInput, 
        df_src_avro_CustsDatasetInput
    )
    df_Subgraph_1_2_out0, df_Subgraph_1_2_target1 = Subgraph_1_2(
        spark, 
        Config.Subgraph_1_2, 
        df_Subgraph_1_1_out0, 
        df_Subgraph_1_1_target1
    )
    df_Subgraph_2_1_2 = Subgraph_2_1_2(spark, Config.Subgraph_2_1_2, df_Subgraph_2_1_1)
    df_Subgraph_2_1_3 = Subgraph_2_1_3(spark, Config.Subgraph_2_1_3, df_Subgraph_2_1_2)
    df_Subgraph_2_2 = Subgraph_2_2(spark, Config.Subgraph_2_2, df_Subgraph_2_1_3)
    df_Subgraph_2_1_4 = Subgraph_2_1_4(spark, Config.Subgraph_2_1_4, df_Subgraph_2_2)
    df_Subgraph_2_1_1_1 = Subgraph_2_1_1_1(spark, Config.Subgraph_2_1_1_1, df_Subgraph_2_1_4)
    df_src_avro_CustsDatasetInput_1 = src_avro_CustsDatasetInput_1(spark)
    df_Subgraph_2_1_2_1 = Subgraph_2_1_2_1(spark, Config.Subgraph_2_1_2_1, df_Subgraph_2_1_1_1)
    df_Subgraph_2_1_3_1 = Subgraph_2_1_3_1(spark, Config.Subgraph_2_1_3_1, df_Subgraph_2_1_2_1)
    df_identity_transform_1 = identity_transform_1(spark, df_src_avro_CustsDatasetInput_1)
    df_Subgraph_1_3_out0, df_Subgraph_1_3_target1 = Subgraph_1_3(
        spark, 
        Config.Subgraph_1_3, 
        df_src_avro_CustsDatasetInput
    )
    df_Subgraph_1_out0, df_Subgraph_1_target1 = Subgraph_1(spark, Config.Subgraph_1, df_src_avro_CustsDatasetInput)
    df_multi_join = multi_join(
        spark, 
        df_Subgraph_1_3_target1, 
        df_Subgraph_1_target1, 
        df_Subgraph_1_1_target1, 
        df_Subgraph_1_2_target1, 
        df_Subgraph_1_1_target1
    )
    df_TRANSORMERS_1 = TRANSORMERS_1(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pipeline123")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipeline123")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipeline123", config = Config)(pipeline)

if __name__ == "__main__":
    main()
