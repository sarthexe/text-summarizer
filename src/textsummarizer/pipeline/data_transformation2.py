from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_transformation import DataTransformation
from src.textsummarizer.logging import logging

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_tranformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.convert()