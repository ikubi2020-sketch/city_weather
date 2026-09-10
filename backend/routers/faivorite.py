from fastapi import APIRouter
from service.faivorites_serv import add_to_favorite_serv

router = APIRouter(prefix="/weather/favorites", tags=["weather"])
