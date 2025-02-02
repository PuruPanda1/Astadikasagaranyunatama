from django.shortcuts import render
from .modules.api_module import get_location_parameters
from .utils.point import Point
from .forms import LatLongForm
from server.utils.tools import haversine
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


@api_view(["POST"])
def get_points_x(request):
    path = [
        {
            "latitude": 5.926,
            "longitude": 80.108,
            "direction": "",
            "location_parameters": {}
        },
        {
            "latitude": 5.934993,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 5.09,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 19.116599900745438
            }
        },
        {
            "latitude": 5.943986000000001,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 5.09,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 18.11662936303665
            }
        },
        {
            "latitude": 5.952979000000001,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 5.09,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 17.11665946066737
            }
        },
        {
            "latitude": 5.961972000000001,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.77,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 16.116690311897678
            }
        },
        {
            "latitude": 5.970965000000001,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.77,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 15.116722066279113
            }
        },
        {
            "latitude": 5.979958000000002,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.77,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 14.116754915737326
            }
        },
        {
            "latitude": 5.988951000000002,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.77,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 13.116789110724035
            }
        },
        {
            "latitude": 5.997944000000002,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.42,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 12.116824984366746
            }
        },
        {
            "latitude": 6.006937000000002,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.42,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 11.116862989651814
            }
        },
        {
            "latitude": 6.015930000000003,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.42,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 10.116903758658433
            }
        },
        {
            "latitude": 6.024923000000003,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.42,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 9.116948200772814
            }
        },
        {
            "latitude": 6.033916000000003,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.02,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 8.11699767349621
            }
        },
        {
            "latitude": 6.042909000000003,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.02,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 7.117054297239958
            }
        },
        {
            "latitude": 6.051902000000004,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 4.02,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 6.117121578858095
            }
        },
        {
            "latitude": 6.060895000000004,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 3.59,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 5.117205766192291
            }
        },
        {
            "latitude": 6.069888000000004,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 3.59,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 4.117319176226517
            }
        },
        {
            "latitude": 6.078881000000004,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 3.59,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 3.1174899272723025
            }
        },
        {
            "latitude": 6.087874000000005,
            "longitude": 80.108,
            "direction": "North",
            "location_parameters": {
                "wind_speed": 3.59,
                "weather_description": "scattered clouds",
                "visibility": 10000,
                "sea_level": 1008,
                "tide_height": 0,
                "distance": 2.11779923427992
            }
        }
    ]
    return Response({"path": path})


@api_view(["POST"])
def get_points(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            points = data.get('points', [])

            if len(points) != 2:
                return Response({"error": "Exactly 2 points are required"}, status=400)

            startPoint, endPoint = points

            # convert to Point objects
            startPoint = Point(
                latitude=float(startPoint['latitude']), longitude=float(startPoint['longitude']))
            endPoint = Point(
                latitude=float(endPoint['latitude']), longitude=float(endPoint['longitude']))

            path = find_min_path(startPoint, endPoint)

            return Response({"path": path})
        except Exception as e:
            return Response({"error": str(e)}, status=400)

    return Response({"error": "Invalid request"}, status=400)


def lat_long_view(request):
    points_path = []

    if request.method == "POST":
        form = LatLongForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            # points_path = find_min_path(Point(latitude=latitude, longitude=longitude))
            start_point = Point(latitude=5.926, longitude=80.108)
            end_point = Point(latitude=6.10691182699255,
                              longitude=80.10855507734915)
            points_path = find_min_path(start_point, end_point)
    else:
        form = LatLongForm()

    return render(request, 'server/lat_long_input.html', {'form': form, 'points_path': points_path})


def find_min_path(startPoint: Point, endPoint: Point):

    current_point = startPoint

    points_path = []

    while (haversine(current_point, endPoint) > 2.0):

        points = find_asta_directions(current_point)

        set_parameters(points, endPoint)

        min_point = choose_min_point(points)

        points_path.append(current_point.to_dict())

        current_point = min_point

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
        data = find_point_s_oceanic_conditions(point, endPoint)
        point.location_parameters.update({
            'wind_speed': data['wind_speed'],
            'weather_description': data['weather_description'],
            'visibility': data['visibility'],
            'sea_level': data['sea_level'],
            'tide_height': data['tide_height'],
            'distance': data['distance']
        })


def find_point_s_oceanic_conditions(point: Point, endPoint: Point):
    distance = haversine(point, endPoint)
    api_data = get_location_parameters(point=point)
    api_data['distance'] = distance
    print(f"Point {point.latitude} & {point.longitude} api data ---> {api_data}")
    print(f"Distance is {distance}")
    return api_data


def choose_min_point(points):

    weights = {
        'wind_speed': 0.1,
        'visibility': 0.2,
        'sea_level': 0.0,
        'tide_height': 0.3,
        'weather_description': 0.0,
        'distance': 0.4
    }

    good_point = find_good_point(points, weights)

    return good_point


def normalize(values, reverse=False):
    """Normalize a list of values to the range [0, 1].
    If reverse is True, higher values will be normalized to lower values."""
    min_val = min(values)
    max_val = max(values)
    if max_val == min_val:
        # All values are the same, return 1 for each
        return [1 for _ in values]
    if reverse:
        return [(max_val - v) / (max_val - min_val) for v in values]
    return [(v - min_val) / (max_val - min_val) for v in values]


def normalize_weights(weights):
    """Normalize weights so that they sum to 1."""
    total_weight = sum(abs(weight) for weight in weights.values())
    return {prop: abs(weight) / total_weight for prop, weight in weights.items()}


def find_good_point(points, weights):
    # Normalize weights so they sum to 1
    normalized_weights = normalize_weights(weights)

    # Extract all property values and normalize them
    normalized_points = {}
    for prop, weight in normalized_weights.items():
        if weight == 0:
            continue  # Skip properties with zero weight

        prop_values = [point.location_parameters[prop] for point in points]

        # Normalize values based on property type
        if prop == "visibility":
            # Higher visibility is better
            normalized_values = normalize(prop_values)
        else:
            normalized_values = normalize(
                prop_values, reverse=True)  # Lower values are better

        # Store normalized values
        for i, norm_val in enumerate(normalized_values):
            normalized_points.setdefault(i, {})[prop] = norm_val

    # Compute weighted scores
    scores = []
    for i, norm_props in normalized_points.items():
        # Only sum over properties that exist in norm_props
        score = sum(norm_props[prop] * normalized_weights[prop]
                    for prop in norm_props.keys())
        scores.append((i, score))

    # Find the point with the best score (highest score is best)
    best_point_index = max(scores, key=lambda x: x[1])[0]
    return points[best_point_index]
