import requests
from logger.logger import logger
from schemas.schem_req import City

def get_city_serv(name) -> dict:
    logger.info("active func | get_city |")
    cites_requested = [] 
    try :
        respond = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name" : name, "count" : 3, "format" : "json" }) 
        respond = respond.json()
        if "results" not in respond: 
            return "no city was found"
        cites_list = respond["results"]
        for city in cites_list:
            cites_requested.append(City(**city))
        return cites_requested
    except Exception as e:
        logger.error(f"reach error {e}")