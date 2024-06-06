from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class damage_codes(models.Model):
    damage_codes_id = models.IntegerField(primary_key = True)
    damage_kodierung = models.CharField(max_length=3)
    damage_kurztext = models.CharField(max_length=32)
    damage_beschreibung = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.damage_kodierung}: {self.damage_kurztext}"
    
    
    