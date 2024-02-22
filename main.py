from text_summarizer.logging import logger
from text_summarizer.pipeline.data_ingestion_stage import DataIngestionTrainingPipeline
from text_summarizer.pipeline.data_transformation_stage import DataTransformationTrainingPipeline
from text_summarizer.pipeline.data_validation_stage import DataValidationTrainingPipeline
from text_summarizer.pipeline.model_trainer_stage import ModelTrainerTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME}...")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f">>>>>> Failed to complete {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME}...")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f">>>>>> Failed to complete {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = 'Data Transformation Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME}...")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f">>>>>> Failed to complete {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = 'Model Training Stage'
try:
    logger.info(f">>>>>> Starting {STAGE_NAME}...")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f">>>>>> Failed to complete {STAGE_NAME}: {e}")
    raise e