# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

if __name__ == '__main__':
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Scale the features (new modification)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split with a different random state
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.25, random_state=123
    )

    # Train a Logistic Regression model (different from your lab)
    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.4f}")

    # Save model to file
    joblib.dump(model, "iris_logistic_model.pkl")
    joblib.dump(scaler, "scaler.pkl")

    print("Training completed — Logistic Regression model saved! by Meena")