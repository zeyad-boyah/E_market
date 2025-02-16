from django.shortcuts import render, HttpResponse

# Create your views here.
def HomePage(request):
    return render(request, template_name="main/home.html")

def ItemsPage (request):
    items= [
        {
            'name': 'Phone',
            'price': '600'
        },
        {
            'name': 'Laptop',
            'price': '1000'
        }
    ]

    
    return render(request, template_name="main/items.html", context={'items':items})