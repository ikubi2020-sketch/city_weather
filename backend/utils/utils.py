from utils.logger import logger 
import requests 
from schemas.schem_req import City
from fastapi import HTTPException

def get_city_utils(city_name, count):
    logger.info("active func | get_city_utils |")
    cites_requested = [] 
    try :
        respond = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name" : city_name, "count" : count, "format" : "json",  "language" : "he"}) 
        respond = respond.json()
        if "results" not in respond: 
            raise HTTPException (status_code=404, detail="no city was found")  
        cites_list = respond["results"]
        for city in cites_list:
            cites_requested.append(City(**city))
        return cites_requested
    except Exception as e:
        logger.error(f"reach error {e}")


def get_whether_by_qour_utils(lat, lon , days = 7):
    logger.info("active func | get_whether_by_id_utils |")
    days_final = {}
    try:
        respond = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude" : lat, "longitude" : lon , "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code",
        "daily" : "temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,weather_code",
        "timezone" : "auto",       
        "forecast_days" : days})    
        respond = respond.json()
        respond = respond["daily"]
        for index, day in enumerate(respond["time"]):
             days_final[day] = {
                  "temperature_max": respond["temperature_2m_max"][index],
                "temperature_min": respond["temperature_2m_min"][index],
                "apparent_temperature_max": respond["apparent_temperature_max"][index],
                "apparent_temperature_min": respond["apparent_temperature_min"][index],
                "weather_code": respond["weather_code"][index],}
        return days_final
    except Exception as e:
            logger.error(f"reach error {e}")
