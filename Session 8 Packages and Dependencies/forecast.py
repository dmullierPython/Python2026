import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 53.8194,
    "longitude": -1.5764,
    "start_date": "2026-11-27",
    "end_date": "2026-12-03",
    "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
    "timezone": "Europe/London",
}

try:
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()
    daily = data["daily"]

    print(f"{'Date':<12} {'Max (°C)':>9} {'Min (°C)':>9} {'Rain (mm)':>10}")
    print("-" * 44)

    # Loop through each of the 7 days returned in the lists
    for i in range(len(daily["time"])):
        date = daily["time"][i]
        temp_max = daily["temperature_2m_max"][i]
        temp_min = daily["temperature_2m_min"][i]
        rain = daily["precipitation_sum"][i]

        print(f"{date:<12} {temp_max:>9} {temp_min:>9} {rain:>10}")

except requests.exceptions.RequestException as err:
    print(f"Could not fetch weather data: {err}")