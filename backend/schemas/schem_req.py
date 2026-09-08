from pydantic import BaseModel

class City(BaseModel):
    name : str 
    latitude : int
    longitude : str