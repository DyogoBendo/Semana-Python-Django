# Generated by Django 2.2.4 on 2020-05-24 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='prioridade',
            field=models.CharField(choices=[('N', 'Normal'), ('B', 'Baixa'), ('A', 'Alta')], max_length=1),
        ),
    ]
