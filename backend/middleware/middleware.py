from pydantic import BaseModel, Field

class Coordinates(BaseModel):
    lat : float = Field(..., ge=-90.0, le = 90.0, description="Latitude must be between -90 and 90")
    lon : float = Field(..., ge=-180.0, le=180.0, description="Longitude must be between -180 and 180" )


class CitiesCompare(BaseModel):
    city1: Coordinates
    city2: Coordinates

