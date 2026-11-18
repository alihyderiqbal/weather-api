import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Weather API", description="Get current weather by city name")

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


@app.get("/")
def home():
    return {"message": "Weather API is running. Visit /docs to try it."}


@app.get("/weather")
def get_weather(city: str):
    # Step A: turn city name into latitude/longitude
    try:
        geo = requests.get(GEO_URL, params={"name": city, "count": 1}, timeout=10)
        geo.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=502, detail="Location service is not responding")

    results = geo.json().get("results")
    if not results:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found")

    place = results[0]

    # Step B: get the weather for that location
    try:
        weather = requests.get(
            WEATHER_URL,
            params={
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "current_weather": True,
            },
            timeout=10,
        )
        weather.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=502, detail="Weather service is not responding")

    current = weather.json()["current_weather"]

    # Step C: send a clean answer
    return {
        "city": place["name"],
        "country": place.get("country"),
        "temperature_c": current["temperature"],
        "wind_speed_kmh": current["windspeed"],
        "time": current["time"],
    }