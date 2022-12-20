import requests

# Set the API endpoint URL and the API key
# url = 'https://api.openweathermap.org/data/2.5/weather'
url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=185811982e2b7b5550443613fb3f0ae4'
#api_key = 'ESTIO_WEATHER_KEY'

# Set the parameters for the API call
params = {
    'q': 'London,uk',  # the city to query
    'units': 'metric',  # use metric units
    'appid': api_key  # your API key
}

# Make a GET request to the API endpoint
response = requests.get(url, params=params)

# Check the status code of the response
if response.status_code == 200:
    # If the status code is 200, the request was successful
    # You can now access the API response data
    data = response.json()
    print(data)
else:
    # If the status code is not 200, the request was not successful
    print('An error occurred:', response.status_code)
