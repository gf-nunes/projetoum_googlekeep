from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notas", default=0)
    titulo = models.CharField(max_length=128, null=True, blank=True)
    texto = models.TextField()


    def __str__(self):
        return self.titulo
