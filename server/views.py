from django.shortcuts import render
from .modules.api_module import get_location_parameters
from .utils.point import Point
from .forms import LatLongForm
from server.utils.tools import haversine
import asyncio


def lat_long_view(request):
    points_path = []

    if request.method == "POST":
        form = LatLongForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            print("Working")
            # points_path = find_min_path(Point(latitude=latitude, longitude=longitude))
            start_point = Point(latitude=5.926, longitude=80.108)
            end_point = Point(latitude=6.10691182699255,
                              longitude=80.10855507734915)
            points_path = find_min_path(start_point, end_point)
    else:
        form = LatLongForm()

    print(len(points_path))
    return render(request, 'server/lat_long_input.html', {'form': form, 'points_path': points_path})


def find_min_path(startPoint: Point, endPoint: Point):

    currentPoint = startPoint

    points_path = []

    while (haversine(currentPoint, endPoint) > 2.0):

        print(f"Current Point: {currentPoint.latitude} & {
              currentPoint.longitude}")

        points = find_asta_directions(currentPoint)

        set_parameters(points, endPoint)

        min_point = choose_min_point(points)

        points_path.append(currentPoint)

        currentPoint = min_point

    return points_path

# * Implemented function to find 8 directions for the given Point


def find_asta_directions(point: Point):
    lat = point.latitude
    long = point.longitude

    latDiff90 = 0.008993
    longDiff90 = 0.008993

    latDiff45 = 0.00637
    longDiff45 = 0.00637

    northPoint = Point(direction='North', latitude=lat +
                       latDiff90, longitude=long)
    northEastPoint = Point(direction='North East',
                           latitude=lat+latDiff45, longitude=long+longDiff45)
    eastPoint = Point(direction='East', latitude=lat,
                      longitude=long+longDiff90)
    southEastPoint = Point(direction='South East',
                           latitude=lat-latDiff45, longitude=long+longDiff45)
    southPoint = Point(direction='South', latitude=lat -
                       latDiff90, longitude=long)
    southWestPoint = Point(direction='South West',
                           latitude=lat-latDiff45, longitude=long-longDiff45)
    westPoint = Point(direction='West', latitude=lat,
                      longitude=long-longDiff90)
    northWestPoint = Point(direction='Noth West',
                           latitude=lat+latDiff45, longitude=long-longDiff45)

    points_list = [
        northPoint,
        northEastPoint,
        eastPoint,
        southEastPoint,
        southPoint,
        southWestPoint,
        westPoint,
        northWestPoint,
    ]

    return points_list


def set_parameters(points, endPoint: Point):
    for point in points:
        data = find_conditions(point, endPoint)
        point.location_parameters.update({
            'wind_speed': data['wind_speed'],
            'weather_description': data['weather_description'],
            'visibility': data['visibility'],
            'sea_level': data['sea_level'],
            'tide_height': data['tide_height'],
            'distance': data['distance']
        })


def find_conditions(point: Point, endPoint: Point):
    distance = haversine(point, endPoint)
    print(f"Distance is {distance}")
    api_data = get_location_parameters(point=point)
    api_data['distance'] = distance
    print(f"Point {point.latitude} & {
          point.longitude} api data ---> {api_data}")
    return api_data


def choose_min_point(points):

    weights = {
        'wind_speed': 0.2,
        'visibility': 0.2,
        'sea_level': 0.1,
        'tide_height': 0.1,
        'weather_description': 0.0,
        'distance': 0.4
    }

    good_point = find_good_point(points, weights)

    return good_point


def normalize(values):
    """Normalize a list of values to the range [0, 1]."""
    min_val = min(values)
    max_val = max(values)
    return [(v - min_val) / (max_val - min_val) if max_val != min_val else 1 for v in values]


def find_good_point(points, weights):
    # Extract all property values and normalize them
    normalized_points = {}
    for prop in weights.keys():
        prop_values = [point.location_parameters[prop] for point in points]

        if prop == "distance":
            max_val, min_val = max(prop_values), min(prop_values)
            normalized_values = [(max_val - val) / (max_val - min_val)
                                 if max_val != min_val else 0 for val in prop_values]
        else:
            normalized_values = normalize(prop_values)

        for i, norm_val in enumerate(normalized_values):
            normalized_points.setdefault(i, {})[prop] = norm_val

    # Compute weighted scores
    scores = []
    for i, norm_props in normalized_points.items():
        score = sum(norm_props[prop] * weights[prop]
                    for prop in weights.keys())
        scores.append((i, score))

    # Find the point with the best score
    best_point_index = max(scores, key=lambda x: x[1])[0]
    return points[best_point_index]


# Usage
# find_min_path(Point(latitude=75, longitude=35), Point(latitude=75.2, longitude=35))

# # Example Usage
# points = [
#     {'height': 5, 'weight': 10, 'density': 20},
#     {'height': 6, 'weight': 8, 'density': 18},
#     {'height': 7, 'weight': 12, 'density': 15}
# ]

# # Weights for properties
# weights = {'height': 0.5, 'weight': 0.3, 'density': 0.2}

# # Find the "good" point
# good_point = find_good_point(points, weights)
# print("Good Point:", good_point)
