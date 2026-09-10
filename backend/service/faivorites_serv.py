import json
from fastapi import HTTPException
from utils.utils  import get_whether_by_qour_utils



def add_to_favorite_serv(user, id, city, lat, lon):
    with open("favorite.json", "r", encoding="utf-8") as f:
        file = json.load(f)
        if user not in file:
            file[user] = [{"id" : id, "city_name" : city,"lat" : lat,"lon" : lon}]
            with open("favorite.json", "w", encoding="utf-8") as f:
                        json.dump(file, f, indent=4)
        else:
            user_in_file = file[user]
            for user_city in user_in_file:
                if user_city["city_name"] == city:
                    raise  HTTPException(status_code=400, detail="city already exists in favorite") 
            file["user"].append({"id" : id, "city_name" : city})
            with open("favorite.json", "w", encoding="utf-8") as f:
                json.dump(file, f, indent=4)
    return "city added"

def get_favorites_serv(user):
    final_favorite = []
    with open("favorite.json", "r", encoding="utf-8") as f:
        file_favorite = json.load(f)
        if user not in file_favorite:
            raise HTTPException(status_code=404, detail="user not found")
        user_favorite = file_favorite[user]
        for city in user_favorite:
             final_favorite.append(get_whether_by_qour_utils(city["lat"], city["lon"]))
        
    return final_favorite 


def remove_form_favorite_serv(user, id):
    id = int(id)
    with open("favorite.json", "r", encoding="utf-8") as f:
        file_favorite = json.load(f)
        if user not in file_favorite:
            raise HTTPException(status_code=404, detail="user not found")
        user_favorite :list = file_favorite[user]
        new_user_favorite = list(filter(lambda city : city["id"] != id, user_favorite))
        if len(user_favorite) == len(new_user_favorite):
             raise HTTPException(status_code=404, detail="city not found")
        file_favorite[user] = new_user_favorite
        with open("favorite.json", "w", encoding="utf-8") as f:
                    json.dump(file_favorite, f, indent=4)
    return f"city {id} was removed" 