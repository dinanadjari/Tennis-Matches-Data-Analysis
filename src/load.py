import glob
import pandas as pd

def to_load(path):
    files = glob.glob(path)
    return pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)

def to_clean(table, min_nonna):
    table.dropna(thresh=min_nonna, inplace=True)
    table.dropna(axis=1, how='all', inplace=True)
