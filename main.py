from creditcard_fraud_detection.logging import logger
from creditcard_fraud_detection.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from creditcard_fraud_detection.pipeline.stage02_data_validation import DataValidationPipeline

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

print("X-----------------------------------------------------------------X")


STAGE_NAME = "Data Validation STAGE"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} Started <<<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<") 
except Exception as e:
    logger.exception(e)
    raise(e)