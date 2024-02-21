from text_summarizer.logging import logger
from text_summarizer.pipeline.data_ingestion_stage import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME}...")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f">>>>>> Failed to complete {STAGE_NAME}: {e}")
    raise e