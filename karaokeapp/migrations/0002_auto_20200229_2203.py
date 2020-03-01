# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karaokeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('note', models.CharField(max_length=200, blank=True)),
                ('start_time', models.DateField(blank=True, null=True)),
                ('end_time', models.DateField(blank=True, null=True)),
                ('insert_time', models.DateField(blank=True, null=True)),
                ('update_time', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('status_name', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.ForeignKey(to='karaokeapp.RoomStatus'),
        ),
    ]
