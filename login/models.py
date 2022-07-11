from django.db import models

class Nota(models.Model):
    titulo = models.CharField(max_length=128, null=True)