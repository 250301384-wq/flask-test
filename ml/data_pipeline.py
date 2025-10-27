import pandas as pd
import logging
from typing import Tuple
import os

logger = logging.getLogger(__name__)

class DataProcessor:
    """??????"""
    
    def __init__(self, data_version: str = "v1"):
        self.data_version = data_version
        self.data_path = f"data/raw/news_{data_version}.csv"
        
    def load_data(self) -> pd.DataFrame:
        """?????"""
        logger.info(f"?????: {self.data_path}")
        
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"??????: {self.data_path}")
            
        df = pd.read_csv(self.data_path)
        logger.info(f"???????: {len(df)} ???")
        return df
    
    def preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """?????"""
        logger.info("???????...")
        
        # ????
        df = df.dropna()
        df = df.drop_duplicates()
        
        # ????????????
        df['title'] = df['title'].astype(str)
        df['content'] = df['content'].astype(str)
        df['category'] = df['category'].astype(str)
        
        logger.info(f"?????: {len(df)} ???")
        return df
    
    def analyze_data(self, df: pd.DataFrame):
        """????"""
        logger.info("=== ????? ===")
        logger.info(f"????: {len(df)}")
        logger.info(f"???: {len(df.columns)}")
        logger.info("\n????:")
        print(df['category'].value_counts())
        
        return df
    
    def run_pipeline(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """???????????"""
        raw_df = self.load_data()
        processed_df = self.preprocess_data(raw_df)
        analyzed_df = self.analyze_data(processed_df)
        return raw_df, analyzed_df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    print("?? v1 ???:")
    processor_v1 = DataProcessor("v1")
    raw_v1, processed_v1 = processor_v1.run_pipeline()
    
    print("\n" + "="*50 + "\n")
    
    print("?? v2 ???:")
    processor_v2 = DataProcessor("v2")
    raw_v2, processed_v2 = processor_v2.run_pipeline()
