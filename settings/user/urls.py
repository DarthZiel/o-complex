from .views import index, register, logout_view
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path("register/", register, name="register"),
    path("logout/", logout_view, name='logout_view'),
]
