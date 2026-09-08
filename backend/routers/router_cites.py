from fastapi import APIRouter
import requests
from service.serv_cites import get_city_serv


router = APIRouter(prefix="/cites", tags=["weather"])


@router.get("/")
def getCity(name : str):
    city = get_city_serv(name)
    return {"status" :200 , "result": city}

