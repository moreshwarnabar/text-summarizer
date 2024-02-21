from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_validation import DataValidation
from text_summarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    
    def main(self):
        config_manager = ConfigurationManager()
        config = config_manager.get_data_validation_config()
        data_validation = DataValidation(config)
        data_validation.validate_all_files_exist()