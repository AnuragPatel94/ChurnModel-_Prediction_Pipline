import requests

url = "http://localhost:8000/predict"

data = {
    "age": 45,
    "tenure_months": 24,
    "monthly_charges": 79.99,
    "total_charges": 1920.00,
    "num_support_calls": 3
}

response = requests.post(url, json=data)
print(response.json())