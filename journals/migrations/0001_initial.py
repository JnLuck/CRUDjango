# Generated by Django 3.2.7 on 2021-11-09 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('tipo', models.CharField(choices=[('PERIODISTA CULTURAL Y SOCIOCULTURAL', 'CULTURAL Y SOCIOCULTURAL'), ('PERIODISTA VIRTUAL', 'VIRTUAL'), ('PERIODISTA  DE INVESTIGACION', 'INVESTIGACION'), ('PERIODISTA DEPORTIVO', 'DEPORTIVO')], max_length=50)),
                ('dni', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Periodista',
                'verbose_name_plural': 'Periodistas',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(choices=[('POLITICA', 'POLITICA'), ('DEPORTIVA', 'DEPORTIVA'), ('ECONOMICA', 'ECONOMICA'), ('CULTURAL', 'CULTURAL'), ('SOCIAL', 'SOCIAL'), ('FARÁNDULA', 'FARÁNDULA'), ('POLICIAL', 'POLICIAL'), ('CIENTIFICA', 'CIENTIFICA')], max_length=50)),
                ('titulo', models.CharField(max_length=255)),
                ('entrada', models.CharField(max_length=500)),
                ('cuerpo', models.CharField(max_length=500)),
                ('cierre', models.CharField(max_length=500)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='noticia')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('periosdista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journals.periodista')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]