from fastapi import APIRouter
import requests


router = APIRouter(prefix="/weather", tags=["weather"])




@router.get(".health")
def getCity():
    return {"status" :200 , "result": "server alive and well"}




@router.get("/")
def getCity():
    city = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={"name" : "Berlin"})
    return {"status" :200 , "result": city.text}

