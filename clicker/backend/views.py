from django.shortcuts import render
from .models import Core, Boost
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CoreSerializer, BoostSerializer


# Create your views here.
@api_view(['GET'])
def call_click(request):
    core = Core.objects.get(user=request.user)
    core.click()
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

    

