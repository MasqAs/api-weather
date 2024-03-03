import httpx

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
HOURLY = "temperature_2m"


def weather_average(latitude: float, longitude: float, forecast: int) -> float:

    params = {"latitude": latitude, "longitude": longitude, "hourly": "temperature_2m", "forecast_days": forecast}

    # Using httpx to make the GET request
    with httpx.Client() as client:
        response = client.get(OPEN_METEO_URL, params=params)

        # Check if the response status code is 200
        if response.status_code == 200:
            data = response.json()
        else:
            # Handle non-200 responses appropriately
            response.raise_for_status()

    # Extracting the temperature data
    weather_data = data["hourly"]["temperature_2m"]

    # Calculating the average temperature
    average_data = round((sum(weather_data) / len(weather_data)), 2)

    return average_data


def need_umbrella(latitude: float, longitude: float, forecast: int) -> list:

    params = {"latitude": latitude, "longitude": longitude, "hourly": "precipitation_probability", "forecast_days": forecast}

    # Using httpx to make the GET request
    with httpx.Client() as client:
        response = client.get(OPEN_METEO_URL, params=params)

        # Check if the response status code is 200
        if response.status_code == 200:
            data = response.json()
        else:
            # Handle non-200 responses appropriately
            response.raise_for_status()

    # Extracting time and precipitation probability data
    times = data["hourly"]["time"]
    precipitation_probabilities = data["hourly"]["precipitation_probability"]

    # Filtering times where precipitation probability is >= 50
    times_with_high_precipitation = [
        times[i] for i, probability in enumerate(precipitation_probabilities) if probability >= 50
    ]

    return times_with_high_precipitation
