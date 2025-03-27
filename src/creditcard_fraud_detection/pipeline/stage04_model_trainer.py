from creditcard_fraud_detection.config.configuration import ConfigurationManager
from creditcard_fraud_detection.components.model_trainer import ModelTrainer
from creditcard_fraud_detection.logging import logger



class ModelTrainerPipeline():
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_config = config.get_model_config()
            model_trainer = ModelTrainer(config=model_config)
            model_trainer.train()
        except Exception as e:
            raise e
