from fastapi import APIRouter

router = APIRouter(prefix="/weather/", tags=["weather"])




@router.get("health")
def health_check():
    return {"status" :200 , "result": "server alive and well"}


