from creditcard_fraud_detection.components.data_transformation import DataTransformation
from creditcard_fraud_detection.logging import logger
from creditcard_fraud_detection.config.configuration import ConfigurationManager
class DataTransformationPipeline():
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e