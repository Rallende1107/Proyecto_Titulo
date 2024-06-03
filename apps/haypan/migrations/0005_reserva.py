# Generated by Django 5.0.6 on 2024-05-31 20:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haypan', '0004_remove_usuario_unique_username_for_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroOrden', models.IntegerField(unique=True)),
                ('fechaInicio', models.DateField()),
                ('estado', models.CharField(choices=[('1', 'Solicitado'), ('2', 'En Espera'), ('3', 'Retirado'), ('4', 'Cancelado Cliente'), ('5', 'Cancelado Comerciante'), ('6', 'Expirado')], default='1', max_length=1)),
                ('cliente', models.ForeignKey(limit_choices_to={'cliente': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haypan.local')),
                ('productos', models.ManyToManyField(to='haypan.producto')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'db_table': 'Reserva',
                'managed': True,
            },
        ),
    ]
