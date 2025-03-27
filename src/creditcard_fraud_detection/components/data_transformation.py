import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from creditcard_fraud_detection.logging import logger
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from creditcard_fraud_detection.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
    
    def create_features(self):
        df = pd.read_csv(os.path.join(self.config.data_path, 'creditcard.csv'))
        ## rescaling Amount and time
        df['Amount'] = RobustScaler().fit_transform(df['Amount'].to_numpy().reshape(-1,1))
        time = df['Time']
        df['Time'] = (time-time.min())/(time.max()-time.min())
        df = df.sample(frac=1, random_state=1)

        df_np = df.to_numpy()
        y=df_np[:,-1]
        X = df_np[:,:-1]
        X_train, X_temp, y_train, y_temp = train_test_split(X,y, test_size=0.3, random_state=42)
        X_test,X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
        logger.info(f"Train Size: {len(y_train)}, Test Size: {len(y_test)}, Val Size: {len(y_val)}")

        train_df = pd.DataFrame(X_train)
        train_df['Class'] = y_train
        
        test_df = pd.DataFrame(X_test)
        test_df['Class'] = y_test

        val_df = pd.DataFrame(X_val)
        val_df['Class'] = y_val

        fraud = df.query('Class == 1')
        not_fraud = df.query('Class == 0')

        balanced_df = pd.concat([fraud, not_fraud.sample(len(fraud), random_state=100)])
        logger.info(f"Created a balanced df of size: {len(balanced_df)}")
        return balanced_df, test_df, val_df
    
    def convert(self):
        train, test, val = self.create_features()
        train.to_csv(os.path.join(self.config.root_dir,'train.csv'))
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'))
        val.to_csv(os.path.join(self.config.root_dir,'val.csv'))
        