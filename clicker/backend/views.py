from django.shortcuts import render
from .models import Core, Boost, AutoBoost
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CoreSerializer, BoostSerializer


# Create your views here.
@api_view(['GET'])
def call_click(request):
    core = Core.objects.get(user=request.user)
    core.click()
    return Response({"core": CoreSerializer(core).data})


@api_view(['GET'])
def get_core_info(request):
    core = Core.objects.get(user=request.user)
    return Response({"core": CoreSerializer(core).data})


@api_view(['POST'])
def get_autoboost(request):
    number = int(request.POST.get("number"))
    core = Core.objects.get(user=request.user)
    booster = AutoBoost.objects.get(core=core, number=number)
    use = booster.use_boost()
    core.refresh_from_db()
    return Response({"status": use, "core": CoreSerializer(core).data, "boost": BoostSerializer(booster).data})


@api_view(['POST'])
def send_click_data(request):
    core = Core.objects.get(user=request.user)
    clicks = int(request.POST.get("clicks"))
    core.click(clicks)
    return Response({"core": CoreSerializer(core).data})


@api_view(['POST'])
def set_coins(request):
    core = Core.objects.get(user=request.user)
    core.set_coins(request.POST.get("money"))
    return Response({"core": CoreSerializer(core).data})



@api_view(['POST'])
def get_boost(request):
    print(request.POST)
    number = int(request.POST.get("number"))
    core = Core.objects.get(user=request.user)
    booster = Boost.objects.get(core=core, number=number)
    use = booster.use_boost()
    core.refresh_from_db()

    return Response({"status": use, "core": CoreSerializer(core).data, "boost": BoostSerializer(booster).data})

    

