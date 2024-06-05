from django.shortcuts import render
from django.http import HttpResponse
from .models import damage_codes

# Create your views here.

def index(request):
    return render(request, "Pic_Catalogue/index.html")

def layout(request):
    return render(request, "Pic_Catalogue/layout.html", {
        "Pic_Catalogue": damage_codes.objects.all()
        })