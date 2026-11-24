import requests

response = requests.get("https://www.leedsbeckett.ac.uk/")
print(response.status_code)
