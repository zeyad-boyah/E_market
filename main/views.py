from django.shortcuts import render, redirect
from main.models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

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
    if request.method == 'GET':
        return render (request, template_name='main/register.html')
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/register.html', {'form': form})