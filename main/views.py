from django.shortcuts import render, HttpResponse

# Create your views here.
def HomePage(request):
    return HttpResponse("<h1>HELLO THERE!!</h1>")