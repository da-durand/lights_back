from django.db import models
from colorfield.fields import ColorField

class Light(models.Model):
    color = ColorField(default='FF0000')
    activate = models.BooleanField()