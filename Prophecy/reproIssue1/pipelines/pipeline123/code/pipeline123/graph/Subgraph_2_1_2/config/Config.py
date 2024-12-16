from pipeline123.graph.Subgraph_2_1_2.Subgraph_1_3_1_1_2.config.Config import (
    SubgraphConfig as Subgraph_1_3_1_1_2_Config
)
from pipeline123.graph.Subgraph_2_1_2.Subgraph_1_4_1_2.config.Config import SubgraphConfig as Subgraph_1_4_1_2_Config
from pipeline123.graph.Subgraph_2_1_2.Subgraph_1_1_1_1_2.config.Config import (
    SubgraphConfig as Subgraph_1_1_1_1_2_Config
)
from pipeline123.graph.Subgraph_2_1_2.Subgraph_1_2_1_1_2.config.Config import (
    SubgraphConfig as Subgraph_1_2_1_1_2_Config
)
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            Subgraph_1_3_1_1_2: dict={},
            Subgraph_1_4_1_2: dict={},
            Subgraph_1_2_1_1_2: dict={},
            Subgraph_1_1_1_1_2: dict={},
            **kwargs
    ):
        self.Subgraph_1_3_1_1_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_3_1_1_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1_3_1_1_2, 
            Subgraph_1_3_1_1_2_Config
        )
        self.Subgraph_1_4_1_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_4_1_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1_4_1_2, 
            Subgraph_1_4_1_2_Config
        )
        self.Subgraph_1_2_1_1_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_2_1_1_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1_2_1_1_2, 
            Subgraph_1_2_1_1_2_Config
        )
        self.Subgraph_1_1_1_1_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_1_1_1_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1_1_1_1_2, 
            Subgraph_1_1_1_1_2_Config
        )
        pass

    def update(self, updated_config):
        self.Subgraph_1_3_1_1_2 = updated_config.Subgraph_1_3_1_1_2
        self.Subgraph_1_4_1_2 = updated_config.Subgraph_1_4_1_2
        self.Subgraph_1_2_1_1_2 = updated_config.Subgraph_1_2_1_1_2
        self.Subgraph_1_1_1_1_2 = updated_config.Subgraph_1_1_1_1_2
        pass

Config = SubgraphConfig()
