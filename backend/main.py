from fastapi import FastAPI
from routers.route_weather  import router as weather
from routers.router_cites import router as city_router
from routers.faivorite import router as faivorite_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(weather)
app.include_router(city_router)
app.include_router(faivorite_router)