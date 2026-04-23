import requests

# The API endpoint you want to call
url = "https://github.com"

# Sending the GET request
response = requests.get(url)

# Check if the reqzxuest was successful (Status Code 200)
if response.status_code == 200:
    # Parse JSON data into a Python dictionary
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")