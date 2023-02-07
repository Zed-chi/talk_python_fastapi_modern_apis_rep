import httpx
import requests

from api.weather.models import Location, Units

API_URL = "https://wttr.in"


def get_report_png(city: str, units: str):
    """Queries wttr.in sesrvice and return png file"""
    url = f"{API_URL}/{city}?{units}=&T="
    response = requests.get(url)
    response.raise_for_status()
    data = response.text

    return data

async def async_get_report_png(city: str, units: str):
    """Queries wttr.in sesrvice and return png file"""
    url = f"{API_URL}/{city}?{units}=&T="
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.text
        return data