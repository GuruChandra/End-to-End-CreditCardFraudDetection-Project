from creditcard_fraud_detection.logging import logger
from creditcard_fraud_detection.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline


logger.info("Welcome to custom logging...")

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} Started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<") 
except Exception as e:
    logger.exception(e)
    raise(e)
