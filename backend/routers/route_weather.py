from fastapi import APIRouter
from service.weather import get_whether_by_quor


router = APIRouter(prefix="/weather", tags=["weather"])




@router.get("/health")
def health_check():
    return {"status" :200 , "result": "server alive and well"}




@router.get("/by_quorditets")
def get_city_by_quor(lan , lat ):
    city = get_whether_by_quor(lan, lat)
    return {"status" :200 , "result": city}




