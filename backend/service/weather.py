import requests
from utils.logger import logger
from utils.utils import get_city_utils
from utils.utils import get_whether_by_qour_utils


def get_whether_by_quor(lan , lat):
    city_weather = get_whether_by_qour_utils(lan , lat)
    return city_weather