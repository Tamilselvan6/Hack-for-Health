# data_preprocessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    # Assuming 'target' is the column you want to predict (e.g., disease presence)
    X = df.drop('target', axis=1)
    y = df['target']

    # Replace missing values, encode categorical variables, etc.
    # Example: Handling missing values by filling them with the mean
    X.fillna(X.mean(), inplace=True)

    # Standardize numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X.select_dtypes(include=['float64']))

    # Concatenate scaled features with non-scaled features
    X = pd.concat([X.drop(X.select_dtypes(include=['float64']).columns, axis=1), pd.DataFrame(X_scaled)], axis=1)

    return X, y
