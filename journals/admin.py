from django.contrib import admin

from journals.models import Noticia, Periodista

# Register your models here.

admin.site.register(Periodista)
admin.site.register(Noticia)

