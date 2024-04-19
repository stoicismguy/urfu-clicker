from django.shortcuts import render
from .models import Core
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CoreSerializer


# Create your views here.
@api_view(['GET'])
def call_click(request):
    core = Core.objects.get(user=request.user)
    core.click()
    return Response({"core": CoreSerializer(core).data})


@api_view(['POST'])
def get_boost(request):
    print(request.POST)
    price = int(request.POST.get("price"))
    power = int(request.POST.get("power"))
    core = Core.objects.get(user=request.user)
    if core.coins >= price:
        core.coins -= price
        core.click_power += power
        core.save()
        return Response({"status": "good", "core": CoreSerializer(core).data})
    return Response({"status": "bad"})
    

