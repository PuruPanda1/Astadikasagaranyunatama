from django.urls import path
from .views import lat_long_view

urlpatterns = [
    path('lat-long/', lat_long_view, name='lat_long_view'),
]
