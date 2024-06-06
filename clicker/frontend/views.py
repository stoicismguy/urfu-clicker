from django.shortcuts import render, redirect
from django.http import HttpResponse
from backend.models import Core, Boost, AutoBoost
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    core = Core.objects.get(user=request.user)
    boosts = Boost.objects.filter(core=core)
    autoboosts = AutoBoost.objects.filter(core=core)
    return render(request, 'index.html', {"coins": core.coins,
                                          "boosts": boosts,
                                          "autoboosts": autoboosts,
                                          "power": core.click_power,
                                          "autoclick_power": core.autoclick_power,
                                          "username": request.user.username})
