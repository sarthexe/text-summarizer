from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.model_evaluation import ModelEvaluation
from src.textsummarizer.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evalution_config()
        model_evaluation_config=ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()