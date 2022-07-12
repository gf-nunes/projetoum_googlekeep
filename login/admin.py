from django.contrib import admin

from .models import Usuario, Nota

# Register your models here.
admin.site.register(Nota)
admin.site.register(Usuario)