from src.ingest import load_csv,to_process
from src.preprocess import process_data
import os
import pandas as pd

raw_path=os.path.join("data","raw","imdb-movies-dataset.csv")
process_path=os.path.join("data","processed","imdb-movies-dataset.parquet")
'''df=load_csv(raw_path)
df=process_data(df)
to_process(df,process_path)'''





d=pd.read_csv(raw_path)
d.drop_duplicates(inplace=True)
d.columns=[col.replace("(min)",'') for col in d.columns]
d.columns=d.columns.str.strip().str.lower().str.replace(" ","_")
d.fillna({"certifacate":"not known","genre":"not known","director":"Not known"},inplace=True)
d["year"]=d["year"].ffill()
d["duration"]=d["duration"].fillna(d["duration"].mean())
d["main_genre"]=d["genre"].apply(lambda x:x.split(",")[0])
print(d.dtypes)
print(d["main_genre"].tail(10))