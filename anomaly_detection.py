# Sai

############################################################################### UNDER CONSTRUCTION PLEASE IGNORE #############################################################################

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Sample patient vitals (synthetic data)
np.random.seed(42)
bp = np.random.normal(120, 10, 200)   # blood pressure
hr = np.random.normal(75, 8, 200)     # heart rate

# Add anomalies
bp = np.concatenate([bp, [200, 40, 180]])
hr = np.concatenate([hr, [30, 190, 20]])

data = pd.DataFrame({"BloodPressure": bp, "HeartRate": hr})

# Isolation Forest
model = IsolationForest(contamination=0.02, random_state=42)
data["anomaly"] = model.fit_predict(data[["BloodPressure", "HeartRate"]])
data["anomaly"] = data["anomaly"].map({1: "Normal", -1: "Anomaly"})

# Plot
plt.figure(figsize=(8,6))
plt.scatter(
    data[data["anomaly"]=="Normal"]["BloodPressure"],
    data[data["anomaly"]=="Normal"]["HeartRate"],
    c="blue", label="Normal", alpha=0.6
)
plt.scatter(
    data[data["anomaly"]=="Anomaly"]["BloodPressure"],
    data[data["anomaly"]=="Anomaly"]["HeartRate"],
    c="red", label="Anomaly", marker="x", s=100
)
plt.xlabel("Blood Pressure")
plt.ylabel("Heart Rate")
plt.title("Anomaly Detection (Isolation Forest)")
plt.legend()
plt.show()

# Print anomalies
print("Detected anomalies:")
print(data[data["anomaly"]=="Anomaly"])
