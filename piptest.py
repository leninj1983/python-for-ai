import requests

url = "https://open.er-api.com/v6/latest/SGD"
response = requests.get(url)
data = response.json()

print("Status:", response.status_code)
print("Last updated:", data["time_last_update_utc"])
print()

for currency in ["INR", "USD", "VND", "JPY", "IDR"]:
    rate = data["rates"][currency]
    print(f"1 SGD = {rate:,.2f} {currency}")