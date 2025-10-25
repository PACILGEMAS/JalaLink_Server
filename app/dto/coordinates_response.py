from pydantic import BaseModel


class CoordinatesResponse(BaseModel):
    latitude: float
    longitude: float
    distance: float
