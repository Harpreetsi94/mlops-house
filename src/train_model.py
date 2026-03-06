import joblib
from sklearn.linear_model import LinearRegression
from utils import load_data, split_features_target

DATA_PATH = "D:\mlops-project/data/house_data.csv"
MODEL_PATH = "D:\mlops-project/models/model.pkl"

def train():

    df = load_data(DATA_PATH)

    X, y = split_features_target(df)

    model = LinearRegression()

    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)

    print("Model saved successfully")

if __name__ == "__main__":
    train()