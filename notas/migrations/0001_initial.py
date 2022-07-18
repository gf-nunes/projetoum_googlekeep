# Generated by Django 4.0.6 on 2022-07-18 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=128, null=True)),
                ('texto', models.TextField()),
                ('usuario', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='notas.usuario')),
            ],
        ),
    ]