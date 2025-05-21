import os
import pandas as pd

def load_csv(data)->pd.DataFrame:
    if os.path.exists(data):
        to_df=pd.read_csv(data)
    return to_df

def to_process(data:pd.DataFrame,path):
    os.mkdir(os.path.dirname(path))
    print(f"Parquet file is saved at :{path}")
    data.to_parquet(path)
    
