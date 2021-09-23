import requests
import json
import pandas as pd

def get_velib_data(cols=None):
    raw = requests.get("https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json?maxfeatures=500&start=1")
    data = json.loads(raw.text)["values"]
    df = pd.DataFrame(data)

    if cols is None :
        return df
    else:
        return df[cols]