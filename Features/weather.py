import requests

# AccuWeather API key
API_KEY = "MC4QwBqMrbFnbQZ40aiAtSj81p3uQUdL"

# Location information
location_name = input("Enter the city name : ")  # Replace with your desired location name

# Function to get the location key by name
def get_location_key(location_name):
    location_search_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": API_KEY,
        "q": location_name,
    }
    response = requests.get(location_search_url, params=params)
    response.raise_for_status()
    locations = response.json()
    if locations:
        return locations[0]["Key"]
    else:
        return None

# Get location key for the specified location name
location_key = get_location_key(location_name)

if location_key:
    # AccuWeather API endpoints
    base_url = "http://dataservice.accuweather.com"
    current_conditions_url = f"{base_url}/currentconditions/v1/{location_key}"
    indices_url = f"{base_url}/indices/v1/daily/1day/{location_key}"

    # Function to make API requests
    def get_data(url, params=None):
        params = params or {}
        params["apikey"] = API_KEY

        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # Get current conditions
    current_conditions = get_data(current_conditions_url)
    if current_conditions:
        weather_data = current_conditions[0]

        # Extract relevant information
        temperature = weather_data["Temperature"]["Metric"]["Value"]
        weather_text = weather_data["WeatherText"]

        print(f"Current Weather in {location_name}:")
        print(f"Weather: {weather_text}")
        print(f"Temperature: {temperature}°C")


    # Get Minute Cast (Precipitation forecast)

    # Get health and activities indices
    indices_data = get_data(indices_url)
    if indices_data:
        health_index = indices_data[0]["Category"]
        dust_dander_index = indices_data[1]["Category"]
        arthritis_index = indices_data[2]["Category"]
        mosquitoes_index = indices_data[3]["Category"]

        print("\nHealth and Activities Indices (Today):")
        print(f"Health Index: {health_index}")
        print(f"Dust and Dander Index: {dust_dander_index}")
        print(f"Arthritis Index: {arthritis_index}")
        print(f"Mosquitoes Index: {mosquitoes_index}")
else:
    print(f"Location '{location_name}' not found.")