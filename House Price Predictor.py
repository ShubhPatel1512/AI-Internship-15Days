import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ------------------------------------
# Step 1: Create Dataset
# ------------------------------------

data = {
    "Area": [1000, 1200, 1500, 1800, 2000,
             2500, 3000, 3500, 4000, 4500],

    "Bedrooms": [2, 2, 3, 3, 3,
                 4, 4, 4, 5, 5],

    "Location": ["CityA", "CityA", "CityB", "CityB", "CityA",
                 "CityC", "CityC", "CityB", "CityC", "CityA"],

    "Price": [30, 35, 50, 55, 60,
              80, 95, 90, 120, 130]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# ------------------------------------
# Step 2: Encode Location
# ------------------------------------

location_mapping = {
    "CityA": 0,
    "CityB": 1,
    "CityC": 2
}

df["Location"] = df["Location"].map(location_mapping)

print("\nEncoded Dataset")
print(df)

# ------------------------------------
# Step 3: Define Features and Target
# ------------------------------------

X = df[["Area", "Bedrooms", "Location"]]

y = df["Price"]

# ------------------------------------
# Step 4: Split Dataset
# ------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ------------------------------------
# Step 5: Train Model
# ------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# ------------------------------------
# Step 6: Make Predictions
# ------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------
# Step 7: Evaluate Model
# ------------------------------------

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("--------------------")
print("Mean Squared Error =", round(mse, 2))
print("R² Score =", round(r2, 4))

# ------------------------------------
# Step 8: User Prediction
# ------------------------------------

print("\nEnter House Details")

area = float(input("Enter Area: "))
bedrooms = int(input("Enter Bedrooms: "))
location = int(input("Location (0=CityA, 1=CityB, 2=CityC): "))

new_house = [[area, bedrooms, location]]

predicted_price = model.predict(new_house)

print("\nPredicted House Price =",
      round(predicted_price[0], 2),
      "Lakhs")