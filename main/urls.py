from django.urls import path
from main.views import HomePage, ItemsPage


urlpatterns = [
    path('home/', HomePage , name="home"),
    path('items/', ItemsPage , name="all_items")
]