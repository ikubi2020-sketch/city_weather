from logger import logger 
import requests
from schemas.schem_req import City

def get_city_utils(city_name):
    logger.info("active func | get_city_utils |")
    cites_requested = [] 
    try :
        respond = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name" : city_name, "count" : 10, "format" : "json" }) 
        respond = respond.json()
        if "results" not in respond: 
            return "no city was found"
        cites_list = respond["results"]
        for city in cites_list:
            cites_requested.append(City(**city))
        return cites_requested
    except Exception as e:
        logger.error(f"reach error {e}")