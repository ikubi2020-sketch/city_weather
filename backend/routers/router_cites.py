from fastapi import APIRouter
import requests
from service.serv_cites import get_city_serv


router = APIRouter(prefix="/weather/cites", tags=["city"])


@router.get("/")
def get_city(name : str):
    city = get_city_serv(name)
    return {"status" :200 , "result": city}

