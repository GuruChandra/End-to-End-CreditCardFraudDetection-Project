from creditcard_fraud_detection.constants import *
from creditcard_fraud_detection.utils.common import read_yaml, create_directories
from creditcard_fraud_detection.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from creditcard_fraud_detection.entity import Model_Config

class ConfigurationManager:
    def __init__(
            self,
            config_file_path = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation(self)-> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    
    def get_data_transformation(self)->DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config

    def get_model_config(self)-> Model_Config:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])
        model_config = Model_Config(
            root_dir=config.root_dir,
            data_path=config.data_path,
            n_estimators=params.n_estimators,
            max_depth=params.max_depth
        )
        return model_config
