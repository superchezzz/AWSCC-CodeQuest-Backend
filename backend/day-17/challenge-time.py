import requests

url = "https://jsonplaceholder.typicode.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Request successful.")
else:
    print("Request failed.")
