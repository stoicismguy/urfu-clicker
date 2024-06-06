from django.urls import path
from .views import *

urlpatterns = [
    path("call_click/", call_click),
    path("get_boost/", get_boost, name='boost'),
    path("get_autoboost/", get_autoboost, name='autoboost'),
    path("get_core_info/", get_core_info, name='core_info'),
    path("send_click_data/", send_click_data, name='send_click_data'),
    path("set_coins/", set_coins, name='set_coins'),
]