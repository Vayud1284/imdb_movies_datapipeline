import unittest
import os 
import pandas as pd
from src.preprocess import process_data

class TestPreprocess(unittest.TestCase):
    def test_process_data(self):
        data={
            "poster":["asdf","fdsa",None ,"jkl"],
            "title" :["nhd","vayud","pandey","jdj"],
            "duration (min)":[30.0,58.0,None,55],
            "Year": [2021.0,None,2025.0,2012.0],
            "genre":["rom,com,thriller","thriller,rom","com","murder,com,thriller"],
            "review_count":["1.5","40","6.2","6.0"],
            "votes":["1.5","40","6.2","6.0"]
        }
        df=pd.DataFrame(data)
        processed_df=process_data(df)
        print(processed_df)
if __name__ == '__main__':
    unittest.main()