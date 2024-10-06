"""
Definition of forms.
"""

from django import forms
from .models import EnKode
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import CheckboxInput

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    

class inputKodeAssi(forms.Form):
    leitung_bol = forms.NullBooleanField(label="", widget=forms.RadioSelect(choices=[(True, 'Leitung'),(False,'Knoten')]), initial=True)
    en_hauptkode_b = forms.ChoiceField(choices=[(obj.en_id, f"{obj.en_hauptkode} - {obj.en_lang}") for obj in EnKode.objects.using('KodeDB').filter(en_kap = "B")], label="Hauptkode")
    en_hauptkode_d = forms.ChoiceField(choices=[(obj.en_id, f"{obj.en_hauptkode} - {obj.en_lang}") for obj in EnKode.objects.using('KodeDB').filter(en_kap = "D")], label="Hauptkode")

    verbindung_bol = forms.NullBooleanField(label="Verbindung", widget=forms.CheckboxInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['en_hauptkode_b'].widget.choices = [(value[0], value[1]) for value in self.fields['en_hauptkode_b'].widget.choices]
        self.fields['en_hauptkode_d'].widget.choices = [(value[0], value[1]) for value in self.fields['en_hauptkode_d'].widget.choices]
