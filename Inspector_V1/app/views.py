"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.models import EnKapitel, EnKode, EnC1, EnC2, EnQ1, EnQ2, EnBeispiele, EnBeispielkode, EnVideobeispiele, EnVideobeispielekode
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
            'title':'Kontakt',
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
            'title':'Über',
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
    en_kode_kapitel = EnKapitel.objects.using('KodeDB').all()
    en_lang = EnKode.objects.using('KodeDB').all()
    en_filtrd = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_hauptkode
    en_kt = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_lang
    en_bschr = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_beschreibung
    en_lage = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_lagetext
    en_c1_text = EnC1.objects.using('KodeDB').filter(enc1_child=kodes_id).values('enc1_kurz', 'enc1_text', 'enc1_lang')
    en_c1_bo = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_c1
    en_c1_be = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_c1text
    en_l1_bo = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_l1
    en_c2_text = EnC2.objects.using('KodeDB').filter(enc2_child=kodes_id).values('enc2_kurz', 'enc2_text', 'enc2_lang')
    en_c2_bo = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_c2
    en_c2_be = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_c2text
    en_l2_bo = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_l2
    en_sa_bo = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_sa
    en_q1_text = EnQ1.objects.using('KodeDB').filter(enq1_child=kodes_id).values('enq1_dim', 'enq1_kurz', 'enq1_lang')
    en_q1_bo = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_q1
    en_q1_be = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_q1text
    en_q2_text = EnQ2.objects.using('KodeDB').filter(enq2_child=kodes_id).values('enq2_dim', 'enq2_kurz', 'enq2_lang')
    en_q2_bo = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_q2
    en_q2_be = EnKode.objects.using('KodeDB').get(en_id=kodes_id).en_q2text
    en_beispielKode = EnBeispielkode.objects.using('KodeDB').filter(enk_kode=en_filtrd)

    env_id = EnVideobeispielekode.objects.using('KodeDB').filter(envb_kode = en_filtrd)
    envb_id = []
    for videos in env_id:
        envb_id.append(videos.envb_envid)
    envb_video = EnVideobeispiele.objects.using('KodeDB').filter(env_id__in = envb_id)
    beispieleID = []
    for beispiele in en_beispielKode:
        beispieleID.append(beispiele.enk_enbid)
    enb_bilder = EnBeispiele.objects.using('KodeDB').filter(enb_id__in=beispieleID).exclude(enb_id='87')

    return render(
        request, 
        'app/catalogue_design.html', 
        {
            'kodes': kodes_id,
            'title':'Schadenskatalog',
            'message':'Kodierungen und Schadensbilder.',
            'year':datetime.now().year,
            'en_hauptkode': en_hauptkode,
            'en_kode_kapitel': en_kode_kapitel,
            'en_lang': en_lang,
            'en_filtrd': en_filtrd,
            'kurztext': en_kt,
            'beschreibung': en_bschr,
            'en_lage' : en_lage,
            'en_c1_bo': en_c1_bo,
            'en_l1_bo' : en_l1_bo,
            'en_c1_text' : en_c1_text,
            'en_c1_be' : en_c1_be,
            'en_beispielKode' : en_beispielKode,
            'enb_bilder' : enb_bilder,
            'beispieleID' : beispieleID,
            'en_c2_bo': en_c2_bo,
            'en_l2_bo' : en_l2_bo,
            'en_c2_text' : en_c2_text,
            'en_c2_be' : en_c2_be,
            'en_q1_bo' : en_q1_bo,
            'en_q1_text' : en_q1_text,
            'en_q1_be' : en_q1_be,
            'en_q2_bo' : en_q2_bo,
            'en_q2_text' : en_q2_text,
            'en_q2_be' : en_q2_be,
            'en_sa_bo' : en_sa_bo,

            'env_id' : env_id,
            'envb_video' : envb_video,
            
        }
    )

def pic_fullscreen(request, enb_id):
     enb_bilder = EnBeispiele.objects.using('KodeDB').get(enb_id = enb_id).enb_bild
     enid_bild = EnBeispiele.objects.using('KodeDB').get(enb_id = enb_id).enb_enid
     enids = EnBeispiele.objects.using('KodeDB').filter(enb_enid = enid_bild).exclude(enb_id='87')
     enk_id = EnBeispielkode.objects.using('KodeDB').filter(enk_enbid = enb_id)



     return render(
        request,
        'app/pic_fullscreen.html',
        {
            'title':'Bildkatalog',
            'year':datetime.now().year,
            'enb_bilder':enb_bilder,
            'enids': enids,
            'enk_id' : enk_id,
        }
    )

def vid_fullscreen(request, env_id):
    env_video = f"{EnVideobeispiele.objects.using('KodeDB').get(env_id = env_id).env_video.rsplit('.',1)[0]}.mp4"
    envb_id = EnVideobeispielekode.objects.using('KodeDB').filter(envb_envid = env_id)

    return render(
        request,
        'app/vid_fullscreen.html',
        {
            'title' : 'Videokatalog',
            'year':datetime.now().year,
            'env_id' : env_id,
            'env_video' : env_video,
            'envb_id' : envb_id,
        }
    )

def bildkatalog(request):
    schadensbilder = EnBeispiele.objects.using('KodeDB').order_by('enb_bild').exclude(enb_id='87').all()
    
    return render(
        request,
        'app/bildkatalog.html',
        {
            'title':'Bildkatalog',
            'year':datetime.now().year,
            'schadensbilder': schadensbilder,
            
        }
    )

def stdAnmerkung(request, kodes_id):

    return render(
        request,
        'app/standardAnmerkung.html',
        {
            'title': 'Standard Anmerkung',
            'year' : datetime.now().year,
            'kodes' : kodes_id,
        }
    )