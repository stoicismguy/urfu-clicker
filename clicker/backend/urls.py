from django.urls import path
from .views import *

urlpatterns = [
    path("call_click/", call_click),
    path("get_boost/", get_boost, name='boost'),
]