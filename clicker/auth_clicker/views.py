from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

from backend.models import Core
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
                core.save()
                user = authenticate(request,
                                    username=username,
                                    password=password)
                login(request, user)
                return redirect('main')
            
        form = UserForm()
        return render(request, "register.html", {"form": form})
    

def logout_view(request):
    logout(request)
    return redirect('login')