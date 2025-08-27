from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

# Features: [Packet Length, TTL, UDP Flag, Packet Rate]
X_train = np.array([
    [100, 64, 0, 2],  # Normal TCP traffic
    [500, 50, 0, 3],  # Normal TCP traffic
    [150, 128, 1, 50],  # UDP flood attack (high packet rate)
    [200, 120, 1, 80]   # UDP flood attack (extremely high packet rate)
])
y_train = ["Harmless", "Harmless", "Harmful", "Harmful"]

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "ml_traffic_classifier.pkl")
print("Model retrained and saved as ml_traffic_classifier.pkl")
