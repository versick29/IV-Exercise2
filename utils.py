import pandas as pd
import os

path = "static/data/teamData.csv"

def data_json(path):
    data = pd.read_csv(path)
    
    return data.to_json(os.path.join(os.getcwd(), f"{os.path.splitext(os.path.basename(path))[0]}.json"),orient='index')



def data_conversion_to_JSON():
    folder_path = "static/data"
    files = os.listdir(folder_path)
    for file in files:
        data_json(os.path.join(folder_path, file))
        
