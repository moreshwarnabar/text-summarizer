from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_ingestion import DataIngestion
from text_summarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    
    def main(self):
        config_manager = ConfigurationManager()
        config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()