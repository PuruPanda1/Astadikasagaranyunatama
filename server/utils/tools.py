import math
from server.utils.point import Point

def haversine(p1: Point,  p2: Point):
    R = 6371  # Earth radius in km
    dlat = math.radians(p2.latitude - p1.latitude)
    dlon = math.radians(p2.longitude - p1.longitude)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(p1.latitude)) * math.cos(math.radians(p2.latitude)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c  # Distance in km


def average_height(heights: list):
    return sum(heights) / len(heights)