from fastapi import APIRouter
from service.weather import get_whether_by_quor


router = APIRouter(prefix="/weather", tags=["weather"])




@router.get("/health")
def health_check():
    return {"status" :200 , "result": "server alive and well"}




@router.get("/get_weather")
def get_weather_by_quor(lat, lon):
    city = get_whether_by_quor(lat, lon)
    return {"status" :200 , "result": city}

