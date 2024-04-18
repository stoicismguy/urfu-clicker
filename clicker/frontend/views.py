from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Core
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    core = Core.objects.get(user=request.user)
    return render(request, 'index.html', {"coins": core.coins, "power": core.click_power})
