from django.urls import path
from .views import *

urlpatterns = [
    path('lat-long/', lat_long_view, name='lat_long_view'),
    path('api/get-points/', get_points, name='get_points'),
    path('api/get-points-x/', get_points_x, name='get_points_x'),
]
