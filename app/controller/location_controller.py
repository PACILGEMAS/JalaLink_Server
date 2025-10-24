from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.dto import WebResponse
from app.service import predict_location, nearest_location

router = APIRouter()


@router.get("/locations/predict")
def get_predict_location(lng: float = Query(None), lat: float = Query(None)):
    prediction = predict_location(longitude=lng, latitude=lat)
    response = WebResponse.builder().data(prediction).build()
    return JSONResponse(status_code=200, content=response.dict())


@router.get("/locations/nearest")
def get_nearest_location(lng: float = Query(None), lat: float = Query(None)):
    coordinates = nearest_location(longitude=lng, latitude=lat)
    response = WebResponse.builder().data(coordinates).build()
    return JSONResponse(status_code=200, content=response.dict())
