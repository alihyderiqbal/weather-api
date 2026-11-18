# Weather API

A REST API built with Python and FastAPI that returns the current weather for any city.

## Features
- Search weather by city name
- Error handling for invalid cities (404) and service failures (502)
- Auto-generated API documentation (Swagger UI)

## Tech Used
Python, FastAPI, Uvicorn, Requests, Open-Meteo API

## How to Run
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install packages: `pip install -r requirements.txt`
5. Start the server: `uvicorn main:app --reload`
6. Open http://127.0.0.1:8000/docs in your browser

## Example
Request:
```
GET /weather?city=Lahore
```

Response:
```json
{
  "city": "Lahore",
  "country": "Pakistan",
  "temperature_c": 20.7,
  "wind_speed_kmh": 5.6,
  "time": "2026-11-18T12:30"
}
```

## Live Demo
## Live Demo

The Weather API is deployed on Vercel and available online.

**API Endpoint:**  
https://weather-api-553q.vercel.app/

**Interactive API Documentation (Swagger):**  
https://weather-api-553q.vercel.app/docs
