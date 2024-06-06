"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.models import EnKapitel, EnKode
from django.urls import reverse

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def damages(request):
    """Renders the damages page."""
    assert isinstance(request, HttpRequest)
    en_kode_kapitel = EnKapitel.objects.using('KodeDB').all()
    en_hauptkode = EnKode.objects.using('KodeDB').all()
   
    return render(
        request,
        'app/damages.html', 
        {
            'title':'Schadenskatalog',
            'message':'Kodierungen und Schadensbilder.',
            'year':datetime.now().year,
            'en_kode_kapitel': en_kode_kapitel,
            'en_hauptkode': en_hauptkode,
        }
        
    )

def damages_kodes(request, kodes_id):
    en_hauptkode = EnKode.objects.using('KodeDB').all()
    en_lang = EnKode.objects.using('KodeDB').all()
    en_filtrd = EnKode.objects.using('KodeDB').order_by('en_id')
    
    return render(
        request, 
        'app/catalogue_design.html', 
        {
            'kodes': kodes_id,
            'title':'Schadenskatalog',
            'message':'Kodierungen und Schadensbilder.',
            'year':datetime.now().year,
            'en_hauptkode': en_hauptkode,
            'en_lang': en_lang,
            'en_filtrd': en_filtrd,
        }
    )
