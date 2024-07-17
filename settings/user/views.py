from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from services.user import login_user

# Create your views here.
@login_required
def index(request):
    return render(request, 'user/index.html')


