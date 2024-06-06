from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

from backend.models import Core, Boost, AutoBoost
from django.contrib.auth.models import User
from .forms import UserForm

# Create your views here.
class LoginView(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, "login.html", {"form": form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=request.POST.get("username"),
                                password=request.POST.get("password"))
            if user is not None:
                login(request, user)
                return redirect('main')
            
        form = UserForm()
        return render(request, "login.html", {"form": form})


class RegisterView(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, "register.html", {"form": form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            existing_user = User.objects.filter(username=username)
            # print(existing_user)
            if len(existing_user) == 0:
                password = request.POST.get("password")
                user = User.objects.create_user(username, '', password)
                user.save()
                core = Core.objects.create(user=user)
                create_all_boosters(core)
                
                core.save()
                user = authenticate(request,
                                    username=username,
                                    password=password)
                login(request, user)
                return redirect('main')
            
        form = UserForm()
        return render(request, "register.html", {"form": form})
    

def create_all_boosters(core):
    Boost.objects.create(name="Тестостерон", number=1,core=core,power=1,price=150).save()
    Boost.objects.create(name="Дека", number=2,core=core,power=5,price=650).save()
    Boost.objects.create(name="Метан", number=3,core=core,power=10,price=1300).save()
    Boost.objects.create(name="Сустанон", number=4,core=core,power=25,price=3000).save()
    Boost.objects.create(name="Дианабол", number=5,core=core,power=50,price=5500).save() 

    AutoBoost.objects.create(name="Читинг", number=1, core=core, power=10, price=400)       
    AutoBoost.objects.create(name="Креатин", number=2, core=core, power=40, price=1000)       
    AutoBoost.objects.create(name="Протеин", number=3, core=core, power=100, price=2100)       

    

def logout_view(request):
    logout(request)
    return redirect('login')