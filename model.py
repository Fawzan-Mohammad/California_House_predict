import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


df = pd.read_csv("data/California_housing.csv")

x = df.drop(columns=["target"])
y = df["target"]

print(y.head())

print(" This is the shape of x:", x.shape)
print(" This is the shape of y:", y.shape)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

RF_model = RandomForestRegressor(
    n_estimators=300,
    max_depth=20,
    min_samples_split=2, 
    random_state=42
)

RF_model.fit(x_train, y_train)

RF_pred = RF_model.predict(x_test)

print(f"Test Result for the model using r2_score {r2_score(y_test, RF_pred)}")

joblib.dump(RF_model, "RF_Model.pkl")

print("Model saved Successfully!")


