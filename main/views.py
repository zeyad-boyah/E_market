from django.shortcuts import render
from main.models import Item

# Create your views here.
def home_page(request):
    return render(request, template_name="main/home.html")

def items_page (request):
    items = Item.objects.all()
    return render(request, template_name="main/items.html", context={'items' : items})

def login_page (request):
    return render(request, template_name='main/login.html')

def logout_page (request):
    ...

def register_page (request):
    return render (request, template_name='main/register.html')