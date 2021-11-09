from django.db import models

# Create your models here.

TIPO_PERIODISTA=[
    ('PERIODISTA CULTURAL Y SOCIOCULTURAL','PERIODISTA CULTURAL Y SOCIOCULTURAL'),
    ('PERIODISTA VIRTUAL','PERIODISTA VIRTUAL'),
    ('PERIODISTA  DE INVESTIGACION','PERIODISTA INVESTIGACION'),
    ('PERIODISTA DEPORTIVO','PERIODISTA DEPORTIVO'),
]
class Periodista(models.Model):
    codigo=models.CharField(max_length=10)
    tipo=models.CharField(max_length=50, choices=TIPO_PERIODISTA)
    dni=models.CharField(max_length=8)
    nombre=models.CharField(max_length=255)
    celular=models.CharField(max_length=9)
    email=models.EmailField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Periodista")
        verbose_name_plural = ("Periodistas")

    def __str__(self):
        return self.nombre

TIPO_NOTICIA=[
    ('POLITICA','POLITICA'),
    ('DEPORTIVA','DEPORTIVA'),
    ('ECONOMICA','ECONOMICA'),
    ('CULTURAL','CULTURAL'),
    ('SOCIAL','SOCIAL'),
    ('FARÁNDULA','FARÁNDULA'),
    ('POLICIAL','POLICIAL'),
    ('CIENTIFICA','CIENTIFICA'),
]
class Noticia(models.Model):
    fecha=models.DateField()
    periosdista=models.ForeignKey("Periodista", on_delete=models.CASCADE)
    tipo=models.CharField(max_length=50, choices=TIPO_NOTICIA)
    titulo=models.CharField(max_length=255)
    entrada=models.CharField(max_length=500)
    cuerpo=models.CharField(max_length=500)
    cierre=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to="noticia", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Noticia")
        verbose_name_plural = ("Noticias")

    def __str__(self):
        return self.titulo




    

