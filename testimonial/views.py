from django.shortcuts import render
from django.http import HttpResponse

def testimonial(request):
    return render(request, "testimonial/testimonial.html")

# Create your views here.
