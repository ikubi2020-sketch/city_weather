import requests
from utils.logger import logger
from utils.utils import get_whether_by_qour_utils, get_whether_by_qour_utils


def get_whether_by_quor(lat, lon):
    logger.info("active func | get_whether_by_quor |")
    city_weather = get_whether_by_qour_utils(lat, lon)
    return city_weather



def get_weather_compare_serv(cites_details) -> dict:
    logger.info("active func | get_weather_compare_serv |")
    city1result = get_whether_by_qour_utils(cites_details["city1"]["lat"], cites_details["city1"]["lon"])
    city2result = get_whether_by_qour_utils(cites_details["city2"]["lat"], cites_details["city2"]["lon"])
    return {city1result, city2result}
    