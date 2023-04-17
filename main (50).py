import requests
import matplotlib.pyplot as plt

# Authenticate your app
headers = {
    "Authorization": "Bearer <your_access_token>",
    "Content-Type": "application/json"
}

# Retrieve active energy burned, steps taken, and heart rate data
params = {
    "startDate": "<your_start_date>",
    "endDate": "<your_end_date>",
    "period": "day",
    "types": "HKQuantityTypeIdentifierActiveEnergyBurned,HKQuantityTypeIdentifierStepCount,HKQuantityTypeIdentifierHeartRate"
}

response = requests.get("https://api.apple.com/health/v1/observations/query", headers=headers, params=params)

# Extract data from response
data = response.json()["data"]
steps = []
energy_burned = []
heart_rate = []

for item in data:
    if item["type"] == "HKQuantityTypeIdentifierStepCount":
        steps.append(item["value"])
    elif item["type"] == "HKQuantityTypeIdentifierActiveEnergyBurned":
        energy_burned.append(item["value"])
    elif item["type"] == "HKQuantityTypeIdentifierHeartRate":
        heart_rate.append(item["value"])

# Create scatter plot of steps taken in correlation with heart rate
plt.scatter(steps, heart_rate)
plt.xlabel("Steps")
plt.ylabel("Heart Rate")
plt.show()

# Create scatter plot of active energy burned in correlation with steps taken
plt.scatter(steps, energy_burned)
plt.xlabel("Steps")
plt.ylabel("Active Energy Burned")
plt.show()
