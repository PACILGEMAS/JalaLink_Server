from pathlib import Path

import joblib
import numpy as np
from sklearn.neighbors import BallTree

from app.dto import CoordinatesResponse


class MLP:
    _instance = None

    @classmethod
    def get_model(cls):
        if cls._instance is None:
            current_dir = Path(__file__).resolve()
            project_root = current_dir.parents[2]
            model_path = project_root / "model.pkl"
            cls._instance = joblib.load(model_path)
        return cls._instance

def predict_location(latitude: float, longitude: float) -> bool:
    X = np.array([[latitude, longitude]])
    pred = MLP.get_model().predict(X)[0]
    return bool(pred)


def nearest_location(latitude: float, longitude: float) -> CoordinatesResponse:
    locations = np.array([
        [-6.0705, 106.791],
        [-6.0260, 106.755],
        [-6.0180, 106.840],
        [-6.0300, 106.880],
    ])

    locations_rad = np.radians(locations)

    tree = BallTree(locations_rad, metric='haversine')

    target = [latitude, longitude]

    target_rad = np.radians(target).reshape(1, -1)

    dist, ind = tree.query(target_rad, k=1)

    distance_km = dist[0][0] * 6371

    closest_location = locations[ind[0][0]]
    latitude = closest_location[0]
    longitude = closest_location[1]

    return CoordinatesResponse(latitude=float(latitude), longitude=float(longitude), distance=distance_km)
