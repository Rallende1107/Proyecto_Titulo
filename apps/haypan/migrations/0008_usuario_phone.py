# Generated by Django 5.0.6 on 2024-06-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haypan', '0007_reserva_horainicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]