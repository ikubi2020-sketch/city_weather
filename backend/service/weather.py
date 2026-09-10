import requests
from utils.logger import logger
from utils.utils import get_city_utils
from utils.utils import get_whether_by_qour_utils


def get_whether_by_quor(lat, lon):
    city_weather = get_whether_by_qour_utils(lat, lon)
    return city_weather


