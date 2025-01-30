import json
from dataclasses import dataclass


@dataclass
class Point:
    def __init__(self, latitude: float, longitude: float, direction: str = '', location_parameters=None):
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees.")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180 degrees.")

        self.direction = direction or ''
        self.latitude = latitude
        self.longitude = longitude
        self.location_parameters = location_parameters or {}

    def __str__(self):
        return f"Point({self.latitude}, {self.longitude}, {self.location_parameters})"

    def to_dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "direction": self.direction,
            "location_parameters": self.location_parameters
        }
