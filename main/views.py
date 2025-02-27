from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, template_name="main/home.html")

def ItemsPage (request):
    
    return render(request, template_name="main/items.html")