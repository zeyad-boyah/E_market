from django.urls import path
from main.views import HomePage


urlpatterns = [
    path('home/', HomePage , name="home")
]