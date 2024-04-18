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
