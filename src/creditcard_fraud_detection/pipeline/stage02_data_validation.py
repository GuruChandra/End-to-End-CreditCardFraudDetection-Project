from creditcard_fraud_detection.logging import logger
from creditcard_fraud_detection.components.data_validation import DataValidation
from creditcard_fraud_detection.config.configuration import ConfigurationManager
from creditcard_fraud_detection.entity import DataValidationConfig

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise e
