from django.db import models

class Nota(models.Model):
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE, related_name="notas", default=0)
    titulo = models.CharField(max_length=128, null=True, blank=True)
    texto = models.TextField()


    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.nome