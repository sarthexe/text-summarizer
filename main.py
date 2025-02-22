from src.textsummarizer.logging import logger
from src.textsummarizer.pipeline.data_ingestion1 import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"stage{STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e