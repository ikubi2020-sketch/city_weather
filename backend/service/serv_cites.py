import requests
from logger.logger import logger
from schemas.schem_req import City

def get_city_serv(name) -> dict:
    logger.info("active func | get_city |")
    try :
        city_requested : City = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name" : name, "count" : 1, "format" : "json" }) 
        return city_requested.text
    except Exception as e:
        logger.error(f"reach error {e}")
        