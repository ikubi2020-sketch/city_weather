from fastapi import FastAPI
from routers.route_weather  import router as routCity
from routers.router_cites import router as city_router

app = FastAPI()

app.include_router(routCity)
app.include_router(city_router)