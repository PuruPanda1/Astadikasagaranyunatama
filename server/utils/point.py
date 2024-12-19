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
    
    # for implenting comparison we need to check whether we need to move lat wise or long wise

    @staticmethod
    def compare_points(point1, point2):
        if(point1.latitude < point2.latitude or point1.longitude < point2.longitude):
            return -1
        elif(point1.latitude > point2.latitude or point1.longitude > point2.longitude):
            return 1
        else :
            return 0