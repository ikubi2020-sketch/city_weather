from fastapi import APIRouter
import requests


router = APIRouter(prefix="/weather/favorites", tags=["weather"])


