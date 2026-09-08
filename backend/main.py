from fastapi import FastAPI
from router.route_base  import router as routCity

app = FastAPI()

app.include_router(routCity)