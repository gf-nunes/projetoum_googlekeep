# Generated by Django 4.0.6 on 2022-07-12 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_nota_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='usuario_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='login.usuario'),
        ),
    ]
