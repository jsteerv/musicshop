# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 16:09
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=12, unique=True)),
                ('descripcion', models.TextField(max_length=12, unique=True)),
                ('tipo', models.CharField(choices=[(b'cassete', b'Cassete'), (b'lp', b'LP'), (b'cd', b'CD'), (b'vhs', b'VHS'), (b'dvd', b'DVD'), (b'otros', b'Otros')], default=b'otros', max_length=7)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=12, unique=True)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('slug', models.SlugField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicshop.Articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField()),
                ('slug', models.SlugField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicshop.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cedula', models.CharField(max_length=12, unique=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicshop.Vendedor'),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicshop.Pedido'),
        ),
    ]
