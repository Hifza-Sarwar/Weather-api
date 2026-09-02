from fastapi import FastAPI
import requests
import os 
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
@app.get("/weather/{city}")
def get_weather(city:str):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(url)
    if response.status_code!=200:
        return{
            "message":"City not found"
        }
    data = response.json()
    return{
        "city":data["name"],
        "tempErature":data["main"]["temp"],
        "description":data["weather"][0]["description"],
        "humidity":data["main"]["humidity"]
    }
