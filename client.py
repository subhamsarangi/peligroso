import requests

# Make a POST request to the login endpoint
login_url = 'http://localhost:8008/auth/login/'
data = {'username': 'admin', 'password': 'root'}
response = requests.post(login_url, data=data)

# Extract the token from the response
token = response.json().get('token')
print(response.text)
# Use the token for authenticated requests
headers = {'Authorization': f'Token {token}'}
get_data_url = 'http://localhost:8008/api/v1/authors/'
response = requests.get(get_data_url, headers=headers)

# Process the response
data = response.json()
