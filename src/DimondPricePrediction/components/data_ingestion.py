
import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

#Configuring data ingestion to save in artifact folder
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        
        try: 
            data=pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv"))) #Read data which is available on our local drive
            logging.info(" i have read dataset as a df")
            
            
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True) # Creating an artifact directory
            data.to_csv(self.ingestion_config.raw_data_path,index=False) # here and we have saved the raw data here
            logging.info(" i have saved the raw dataset in artifact folder") #Logged the same here
            
            logging.info("here i have performed train test split")
            
            train_data,test_data=train_test_split(data,test_size=0.25) #Perform train test split here
            logging.info("train test split completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path,index=False) #Saving the train and test file here in artifact folder
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("data ingestion part completed")
            
            return (
                 
                
                self.ingestion_config.train_data_path, #Returning these values so that we can feed these values to our pre_processing
                self.ingestion_config.test_data_path # component to connect to pipeline
            )
            
            
        except Exception as e:
           logging.info("exception during occured at data ingestion stage")
           raise customexception(e,sys)
    