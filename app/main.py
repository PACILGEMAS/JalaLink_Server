from fastapi import FastAPI

from app.controller import location_controller

app = FastAPI()

app.include_router(location_controller)
