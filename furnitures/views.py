from django.shortcuts import render
from django.http import HttpResponse

def furnitures(request):
    return render(request, "furnitures/furnitures.html")

# Create your views here.
