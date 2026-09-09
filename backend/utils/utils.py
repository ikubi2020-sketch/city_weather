from utils.logger import logger 
import requests 
from schemas.schem_req import City
from fastapi import HTTPException

def get_city_utils(city_name, count):
    logger.info("active func | get_city_utils |")
    cites_requested = [] 
    try :
        respond = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name" : city_name, "count" : count, "format" : "json" }) 
        respond = respond.json()
        if "results" not in respond: 
            raise HTTPException (status_code=404, detail="no city was found")  
        cites_list = respond["results"]
        for city in cites_list:
            cites_requested.append(City(**city))
        return cites_requested
    except Exception as e:
        logger.error(f"reach error {e}")

def get_whether_by_qour_utils(lon , lat):
    logger.info("active func | get_whether_by_id_utils |")
    try:
        respond = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude" : lat, "longitude" : lon , "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code"})    
        respond = respond.json()
        respond = respond.current
        return respond
    except Exception as e:
            logger.error(f"reach error {e}")
    