from src.ingest import load_csv,to_process
from src.preprocess import process_data
import os
import pandas as pd

raw_path=os.path.join("data","raw","imdb-movies-dataset.csv")
process_path=os.path.join("data","processed","imdb-movies-dataset.parquet")
df=load_csv(raw_path)
df=process_data(df)
to_process(df,process_path)





