from pipeline123.graph.Subgraph_2.config.Config import SubgraphConfig as Subgraph_2_Config
from pipeline123.graph.Subgraph_2_1.config.Config import SubgraphConfig as Subgraph_2_1_Config
from pipeline123.graph.Subgraph_2_1_1.config.Config import SubgraphConfig as Subgraph_2_1_1_Config
from pipeline123.graph.Subgraph_1_1.config.Config import SubgraphConfig as Subgraph_1_1_Config
from pipeline123.graph.Subgraph_1_2.config.Config import SubgraphConfig as Subgraph_1_2_Config
from pipeline123.graph.Subgraph_2_1_2.config.Config import SubgraphConfig as Subgraph_2_1_2_Config
from pipeline123.graph.Subgraph_2_1_3.config.Config import SubgraphConfig as Subgraph_2_1_3_Config
from pipeline123.graph.Subgraph_2_2.config.Config import SubgraphConfig as Subgraph_2_2_Config
from pipeline123.graph.Subgraph_2_1_4.config.Config import SubgraphConfig as Subgraph_2_1_4_Config
from pipeline123.graph.Subgraph_2_1_1_1.config.Config import SubgraphConfig as Subgraph_2_1_1_1_Config
from pipeline123.graph.Subgraph_2_1_2_1.config.Config import SubgraphConfig as Subgraph_2_1_2_1_Config
from pipeline123.graph.Subgraph_2_1_3_1.config.Config import SubgraphConfig as Subgraph_2_1_3_1_Config
from pipeline123.graph.Subgraph_1_3.config.Config import SubgraphConfig as Subgraph_1_3_Config
from pipeline123.graph.Subgraph_1.config.Config import SubgraphConfig as Subgraph_1_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            Subgraph_2_1_1: dict=None,
            Subgraph_1_2: dict=None,
            Subgraph_2_1_4: dict=None,
            Subgraph_2_1_1_1: dict=None,
            Subgraph_2_1: dict=None,
            Subgraph_1_1: dict=None,
            Subgraph_2_1_2_1: dict=None,
            Subgraph_2: dict=None,
            Subgraph_2_1_3: dict=None,
            Subgraph_2_1_2: dict=None,
            Subgraph_1_3: dict=None,
            Subgraph_2_2: dict=None,
            Subgraph_1: dict=None,
            Subgraph_2_1_3_1: dict=None,
            **kwargs
    ):
        self.spark = None
        self.update(
            Subgraph_2_1_1, 
            Subgraph_1_2, 
            Subgraph_2_1_4, 
            Subgraph_2_1_1_1, 
            Subgraph_2_1, 
            Subgraph_1_1, 
            Subgraph_2_1_2_1, 
            Subgraph_2, 
            Subgraph_2_1_3, 
            Subgraph_2_1_2, 
            Subgraph_1_3, 
            Subgraph_2_2, 
            Subgraph_1, 
            Subgraph_2_1_3_1
        )

    def update(
            self,
            Subgraph_2_1_1: dict={},
            Subgraph_1_2: dict={},
            Subgraph_2_1_4: dict={},
            Subgraph_2_1_1_1: dict={},
            Subgraph_2_1: dict={},
            Subgraph_1_1: dict={},
            Subgraph_2_1_2_1: dict={},
            Subgraph_2: dict={},
            Subgraph_2_1_3: dict={},
            Subgraph_2_1_2: dict={},
            Subgraph_1_3: dict={},
            Subgraph_2_2: dict={},
            Subgraph_1: dict={},
            Subgraph_2_1_3_1: dict={},
            **kwargs
    ):
        prophecy_spark = self.spark
        self.Subgraph_2_1_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_1_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2_1_1, 
            Subgraph_2_1_1_Config
        )
        self.Subgraph_1_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1_2, 
            Subgraph_1_2_Config
        )
        self.Subgraph_2_1_4 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_1_4_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2_1_4, 
            Subgraph_2_1_4_Config
        )
        self.Subgraph_2_1_1_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_1_1_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2_1_1_1, 
            Subgraph_2_1_1_1_Config
        )
        self.Subgraph_2_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2_1, 
            Subgraph_2_1_Config
        )
        self.Subgraph_1_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1_1, 
            Subgraph_1_1_Config
        )
        self.Subgraph_2_1_2_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_1_2_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2_1_2_1, 
            Subgraph_2_1_2_1_Config
        )
        self.Subgraph_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2, 
            Subgraph_2_Config
        )
        self.Subgraph_2_1_3 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_1_3_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2_1_3, 
            Subgraph_2_1_3_Config
        )
        self.Subgraph_2_1_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_1_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2_1_2, 
            Subgraph_2_1_2_Config
        )
        self.Subgraph_1_3 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_3_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1_3, 
            Subgraph_1_3_Config
        )
        self.Subgraph_2_2 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_2_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2_2, 
            Subgraph_2_2_Config
        )
        self.Subgraph_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_1, 
            Subgraph_1_Config
        )
        self.Subgraph_2_1_3_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_2_1_3_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_2_1_3_1, 
            Subgraph_2_1_3_1_Config
        )
        pass
