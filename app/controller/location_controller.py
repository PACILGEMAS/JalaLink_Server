from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.dto import WebResponse
from app.service import predict_location, nearest_location

router = APIRouter()


@router.get("/locations/predict")
def get_predict_location(lat: float = Query(None), lng: float = Query(None)):
    prediction = predict_location(latitude=lat, longitude=lng)
    response = WebResponse.builder().data(prediction).build()
    return JSONResponse(status_code=200, content=response.dict())


@router.get("/locations/nearest")
def get_nearest_location(lat: float = Query(None), lng: float = Query(None)):
    coordinates = nearest_location(latitude=lat, longitude=lng)
    response = WebResponse.builder().data(coordinates).build()
    return JSONResponse(status_code=200, content=response.dict())
