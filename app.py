from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.components.data_ingestion import DataIngestion
from src.MLPROJECT.components.data_ingestion import DataIngestionConfig

import sys

if __name__ == '__main__':
    logging.info("Execution has started")
    
    try :
        
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e :
        logging.info("Custon Exception")
        raise CustomException(e,sys)