from django.shortcuts import render
from .modules.api_module import get_location_parameters
from .utils.point import Point
from .forms import LatLongForm
from server.utils.tools import haversine
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


use_tide_api = True

@api_view(["POST"])
def get_points_x(request):
    data = json.loads(request.body)
    # points = data.get('points', [])
    weights = data.get('weights', {})
    print(f"Weights are {weights}")
    print(f"Weights are {weights['windWeight']}")
    path = [
    {
        "latitude": 9.1313564969672,
        "longitude": 79.72427765524787,
        "direction": "",
        "location_parameters": {}
    },
    {
        "latitude": 9.1377264969672,
        "longitude": 79.73064765524788,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.04,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 27.966776209778875
        }
    },
    {
        "latitude": 9.1467194969672,
        "longitude": 79.73064765524788,
        "direction": "North",
        "location_parameters": {
            "wind_speed": 7.04,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 27.400364112955273
        }
    },
    {
        "latitude": 9.155712496967201,
        "longitude": 79.73064765524788,
        "direction": "North",
        "location_parameters": {
            "wind_speed": 6.84,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 26.859248515807124
        }
    },
    {
        "latitude": 9.162082496967201,
        "longitude": 79.73701765524788,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 6.98,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 25.892453705083597
        }
    },
    {
        "latitude": 9.168452496967202,
        "longitude": 79.74338765524789,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 6.98,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 24.92792096246336
        }
    },
    {
        "latitude": 9.174822496967202,
        "longitude": 79.74975765524789,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 6.98,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 23.965922320774943
        }
    },
    {
        "latitude": 9.181192496967203,
        "longitude": 79.7561276552479,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 6.98,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 23.00677452999118
        }
    },
    {
        "latitude": 9.187562496967203,
        "longitude": 79.7624976552479,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 6.82,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 22.05084842149319
        }
    },
    {
        "latitude": 9.193932496967204,
        "longitude": 79.7688676552479,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 6.82,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 21.09858066244781
        }
    },
    {
        "latitude": 9.200302496967204,
        "longitude": 79.7752376552479,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.02,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 20.15048861925268
        }
    },
    {
        "latitude": 9.206672496967204,
        "longitude": 79.78160765524791,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.02,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 19.207189296402575
        }
    },
    {
        "latitude": 9.213042496967205,
        "longitude": 79.78797765524791,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.02,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 18.269423658850425
        }
    },
    {
        "latitude": 9.219412496967205,
        "longitude": 79.79434765524792,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 6.89,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 17.338088120069763
        }
    },
    {
        "latitude": 9.225782496967206,
        "longitude": 79.80071765524792,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 6.89,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 16.414275637564927
        }
    },
    {
        "latitude": 9.232152496967206,
        "longitude": 79.80708765524793,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.14,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 15.499329774471052
        }
    },
    {
        "latitude": 9.232152496967206,
        "longitude": 79.81608065524793,
        "direction": "East",
        "location_parameters": {
            "wind_speed": 7.14,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 14.585375306727876
        }
    },
    {
        "latitude": 9.238522496967207,
        "longitude": 79.82245065524793,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.14,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 13.670988718416073
        }
    },
    {
        "latitude": 9.238522496967207,
        "longitude": 79.83144365524794,
        "direction": "East",
        "location_parameters": {
            "wind_speed": 7.14,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 12.75650388160936
        }
    },
    {
        "latitude": 9.244892496967207,
        "longitude": 79.83781365524794,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.41,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 11.842843599277701
        }
    },
    {
        "latitude": 9.251262496967207,
        "longitude": 79.84418365524795,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.27,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 10.943439771268054
        }
    },
    {
        "latitude": 9.257632496967208,
        "longitude": 79.85055365524795,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.27,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 10.062113448004746
        }
    },
    {
        "latitude": 9.257632496967208,
        "longitude": 79.85954665524795,
        "direction": "East",
        "location_parameters": {
            "wind_speed": 7.27,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 9.119615356483445
        }
    },
    {
        "latitude": 9.257632496967208,
        "longitude": 79.86853965524796,
        "direction": "East",
        "location_parameters": {
            "wind_speed": 7.27,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 8.187590924630673
        }
    },
    {
        "latitude": 9.264002496967208,
        "longitude": 79.87490965524796,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.27,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 7.298314412385041
        }
    },
    {
        "latitude": 9.264002496967208,
        "longitude": 79.88390265524797,
        "direction": "East",
        "location_parameters": {
            "wind_speed": 7.54,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 6.361031132439267
        }
    },
    {
        "latitude": 9.264002496967208,
        "longitude": 79.89289565524797,
        "direction": "East",
        "location_parameters": {
            "wind_speed": 7.54,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 5.441324218124918
        }
    },
    {
        "latitude": 9.270372496967209,
        "longitude": 79.89926565524797,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.54,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 4.536282444054203
        }
    },
    {
        "latitude": 9.270372496967209,
        "longitude": 79.90825865524798,
        "direction": "East",
        "location_parameters": {
            "wind_speed": 7.76,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 3.612624739048601
        }
    },
    {
        "latitude": 9.27674249696721,
        "longitude": 79.91462865524798,
        "direction": "North East",
        "location_parameters": {
            "wind_speed": 7.76,
            "weather_description": "broken clouds",
            "visibility": 10000,
            "sea_level": 1009,
            "tide_height": 0,
            "distance": 2.716939470362486
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
            weights = data.get('weights', {})
            
            print(f"Weights are {weights}")
            print(f"Points are {points}")

            global use_tide_api

            if len(points) != 2:
                return Response({"error": "Exactly 2 points are required"}, status=400)

            startPoint, endPoint = points

            print(f"Start point is {startPoint}")
            print(f"End point is {endPoint}")

            # convert to Point objects
            startPoint = Point(
                latitude=float(startPoint['latitude']), longitude=float(startPoint['longitude']))
            endPoint = Point(
                latitude=float(endPoint['latitude']), longitude=float(endPoint['longitude']))

            if haversine(startPoint, endPoint) > 4.0:
                use_tide_api = False

            path = find_min_path(startPoint, endPoint, weights)

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


def find_min_path(startPoint: Point, endPoint: Point, weights: dict):

    current_point = startPoint

    points_path = []

    while (haversine(current_point, endPoint) > 2.0):

        points = find_asta_directions(current_point)

        set_parameters(points, endPoint)

        min_point = choose_min_point(points, weights)

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
    global use_tide_api
    distance = haversine(point, endPoint)
    api_data = get_location_parameters(point=point, use_tide_api=use_tide_api)
    api_data['distance'] = distance
    print(f"Point {point.latitude} & {point.longitude} api data ---> {api_data}")
    print(f"Distance is {distance}")
    return api_data


def choose_min_point(points, weights: dict):
    global use_tide_api

    if use_tide_api:
        tide_weight = float(weights['tideWeight'])
    else:
        tide_weight = 0

    weights = {
        'wind_speed': float(weights['windWeight']),
        'visibility': float(weights['visibilityWeight']),
        'sea_level': float(weights['seaLevelWeight']),
        'tide_height': tide_weight,
        'weather_description': 0.0,
        'distance': float(weights['distanceWeight'])
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
