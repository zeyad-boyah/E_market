from django.urls import path
from main.views import home_page, items_page, login_page, logout_page, register_page


urlpatterns = [
    path("", home_page, name="home"),
    path("items/", items_page, name="items"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("register/", register_page, name="register"),
]
