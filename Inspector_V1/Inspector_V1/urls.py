"""
Definition of urls for Inspector_V1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('Kontakt/', views.contact, name='contact'),
    path('Über/', views.about, name='about'),
    path('Selbsttest/', views.selbsttest, name='selbsttest'),
    path('Schadenskatalog/', views.damages, name='damages'),
    path('Schadenskatalog/<int:kodes_id>/', views.damages_kodes, name='clicked_kode'),
    path('Bildkatalog/', views.bildkatalog, name='bildkatalog'),
    path('Bildkatalog/<int:enb_id>/', views.pic_fullscreen, name='pic_fullscreen'),
    path('Schadenskatalog/<int:kodes_id>/standardAnmerkung/', views.stdAnmerkung, name='stdAnmerkung'),
    path('Videokatalog/<int:env_id>/', views.vid_fullscreen, name='vid_fullscreen'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    
]
