import requests
from utils.logger import logger
from utils.utils import get_city_utils
from schemas.schem_req import City

def get_city_serv(city_name) -> dict:
    logger.info("active func | get_city |")
    list_of_city = get_city_utils(city_name)
    return list_of_city
    