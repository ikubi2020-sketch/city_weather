from fastapi import FastAPI
from routers.route_weather  import router as weather
from routers.router_cites import router as city_router

app = FastAPI()

app.include_router(weather)
app.include_router(city_router)