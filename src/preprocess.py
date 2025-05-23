import pandas as pd

def process_data(data:pd.DataFrame)->pd.DataFrame:

    data.columns=[col.replace("(min)",'') for col in data.columns]

    #converting columns into lower case
    data.columns=data.columns.str.strip().str.lower().str.replace(" ","_")

    #drop the empty title and poster
    data=data.dropna(subset=["poster","title"])
    data.drop_duplicates(inplace=True)

    #convert review counts and votes into float
    data[["review_count","votes"]]=data[["review_count","votes"]].apply(pd.to_numeric, errors="coerce")
    data.fillna({"certifacate":"not known","genre":"not known","director":"Not known"},inplace=True)
    data["year"]=data["year"].ffill()
    data["duration"]=data["duration"].fillna(data["duration"].mean())
    data["main_genre"]=data["genre"].apply(lambda x:x.split(",")[0])
    return data