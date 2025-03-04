from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from main.models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction

def home_page(request):
    return render(request, template_name="main/home.html")

@transaction.atomic
def items_page (request):
    if request.method == "GET":    
        items = Item.objects.all()
        return render(request, template_name="main/items.html", context={'items' : items})
    elif request.method == "POST":
        if not request.user.is_authenticated:
            messages.warning(request, "You need to log in to make a purchase")
            # Redirect to login with 'next' parameter to return here after login
            return redirect(f"{reverse('login')}?next={reverse('items')}")
        purchased_item = request.POST.get('purchased-item') # this gets the id
        if purchased_item:
            try:
                item = Item.objects.get(id=purchased_item)
                if item.owner is None:
                    item.owner = request.user
                    item.save()
                    messages.success(request, f"Successfully purchased {item.name}!")
                else:
                    messages.error(request, "This item is already owned!")
            except Item.DoesNotExist:
                messages.error(request, "Item not found")
        
        return redirect("items")
    

def login_page (request):
    if request.method == "GET":
        return render(request, template_name='main/login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'you logged in {user.username}, Welcome')
            return redirect('items')
        else: 
            error_message = "Invalid username or password."
            return render(request,'main/login.html', {'error': error_message})
        

def logout_page (request):
    logout(request)
    messages.success(request, f'you logged OUT (╥﹏╥)')
    return redirect('login')

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
            messages.success(request, f'you registered {user.username}, Welcome :)')
            return redirect('home')
        else:
            return render(request, 'main/register.html', {'form': form})