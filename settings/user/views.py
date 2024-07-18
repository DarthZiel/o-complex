from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from services.user import register_user
from .forms import UserRegistrationForm


# Create your views here.
@login_required
def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user = register_user(email, password1, password2)
            if user:
                login(request, user)
                messages.success(request, "Регистрация успешно завершилась.")
                return redirect(reverse('index'))

        else:
            messages.error(request, "Регистрация завершилось не успешно.")
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
