# prediction_model.py
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_predict_model(X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple RandomForestClassifier (replace with your actual model)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Evaluate the model (replace with your actual evaluation metrics)
    accuracy = accuracy_score(y_test, predictions)
    print(f'Model Accuracy: {accuracy}')

    # Save the trained model (optional)
    # joblib.dump(model, 'health_model.joblib')

    return model
