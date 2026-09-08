from fastapi import APIRouter

router = APIRouter(prefix="/weather", tags=["weather"])




@router.get("health")
def getCity():
    return {"status" :200 , "result": "server alive and well"}




# @router.get("/")
# def getCity(name : str):
#     return {"status" :200 , "result": city}

