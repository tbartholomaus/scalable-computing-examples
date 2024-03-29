import pandas as pd
import urllib.request

import hashlib
import os

def load_adc_csv(identifier=None):
    """
    Load and cache a CSV data file from the Arctic Data Center
    as a pandas dataframe.
    """
    hashval = hashlib.sha256(bytes(identifier, 'utf-8')).hexdigest()
    path = 'data/' + hashval
    if not os.path.exists("data/"):
        os.mkdir("data/")
    if not os.path.exists(path): # If the file doesn't exist yet at the created path..
        service = "https://arcticdata.io/metacat/d1/mn/v2/object/"
        url = service + identifier
        msg = urllib.request.urlretrieve(url, path)
    df = pd.read_csv(path)
    return df
