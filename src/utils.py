import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def split_features_target(df):
    X = df[['size']]
    y = df['price']
    return X, y