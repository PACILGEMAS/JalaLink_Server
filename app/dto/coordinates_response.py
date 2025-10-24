from pydantic import BaseModel


class CoordinatesResponse(BaseModel):
    longitude: float
    latitude: float
