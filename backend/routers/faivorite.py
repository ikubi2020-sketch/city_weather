from fastapi import APIRouter
from service.faivorites_serv import add_to_favorite_serv, get_favorites_serv, remove_form_favorite_serv
from schemas.schem_req import City

router = APIRouter(prefix="/weather/favorites", tags=["weather"])


@router.post("/{user}/")
def add_to_favorite(user, city : City):
    respond = add_to_favorite_serv(user, city.id, city.name, city.latitude , city.longitude)
    return respond


@router.get("/{user}")
def get_favorites(user):
    favorite = get_favorites_serv(user)
    return favorite


@router.delete("/{id}")
def remove_from_favorite(id):
    result_message = remove_form_favorite_serv(id)
    return result_message

