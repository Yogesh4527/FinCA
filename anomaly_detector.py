# models/anomaly_detector.py
"""
FinCA – XGBoost Anomaly Detector
Detects anomalies in financial data for audit assistance.
Flags unusual transactions, mismatches, and potential errors.
"""

import numpy as np
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler


class AnomalyDetector:
    """XGBoost-based anomaly detection for financial audit."""

    def __init__(self):
        self.model = XGBClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False

    def train(self, X_train, y_train):
        """Train the anomaly detection model."""
        X_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_scaled, y_train)
        self.is_trained = True
        print("AnomalyDetector trained successfully.")

    def predict(self, X):
        """Predict anomalies in financial data."""
        if not self.is_trained:
            raise RuntimeError("Model not trained. Call train() first.")
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def predict_proba(self, X):
        """Return anomaly probability scores."""
        if not self.is_trained:
            raise RuntimeError("Model not trained. Call train() first.")
        X_scaled = self.scaler.transform(X)
        return self.model.predict_proba(X_scaled)[:, 1]


if __name__ == "__main__":
    print("AnomalyDetector module loaded. Training data required.")
