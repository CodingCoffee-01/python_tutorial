import requests

response = requests.get("https://www.google.com")
print(response.status_code)  # Output: 200
print(response.content)  # Output: the HTML content of the Google homepage