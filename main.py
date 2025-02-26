from src.textsummarizer.logging import logger
from src.textsummarizer.pipeline.data_ingestion1 import DataIngestionTrainingPipeline
from src.textsummarizer.pipeline.data_transformation2 import DataTransformationTrainingPipeline
from src.textsummarizer.pipeline.model_trainer3 import ModelTrainerTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"stage{STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_transformation_pipeline=DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Trainer Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e