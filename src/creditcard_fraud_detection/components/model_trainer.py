import os
import pandas as pd
import numpy as np
from creditcard_fraud_detection.logging import logger
from sklearn.ensemble import RandomForestClassifier
import joblib
from creditcard_fraud_detection.entity import Model_Config
from sklearn.metrics import classification_report


class ModelTrainer():
    def __init__(self,config: Model_Config):
        self.config = config
    
    def train(self):
        model = RandomForestClassifier(n_estimators=self.config.n_estimators, 
                                       max_depth=self.config.max_depth)
        train_df = pd.read_csv(os.path.join(self.config.data_path,'train.csv'))
        train_df_np = train_df.to_numpy()
        X_train = train_df_np[:,:-1]
        y_train = train_df_np[:,-1]
        model.fit(X_train, y_train)
        joblib.dump(model,os.path.join(self.config.root_dir, 'model.pkl'))
        logger.info("model result on the traing data is below:")
        logger.info(classification_report(y_train, model.predict(X_train), target_names=["Not fraud", "Fraud"]))

