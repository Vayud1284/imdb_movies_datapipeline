from src.ingest import load_csv,to_process
import os

raw_path=os.path.join("data","raw","imdb-movies-dataset.csv")
process_path=os.path.join("data","processed","imdb-movies-dataset.parquet")
df=load_csv(raw_path)
to_process(df,process_path)
