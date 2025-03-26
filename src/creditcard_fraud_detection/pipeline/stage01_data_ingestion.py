from creditcard_fraud_detection.config.configuration import ConfigurationManager
from creditcard_fraud_detection.components.data_ingestion import DataIngestion
from creditcard_fraud_detection.logging import logger


class DataIngestionTrainingPipeline():
    def __ini__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        