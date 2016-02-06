# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cab_book_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_cab', models.ImageField(upload_to=b'')),
                ('available_cab', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hotel_details_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hotel_name', models.CharField(max_length=500)),
                ('hotel_address', models.CharField(max_length=800)),
                ('rating', models.IntegerField(default=1)),
                ('cab_available', models.CharField(max_length=10)),
                ('review_count', models.IntegerField(default=0)),
                ('special_reservation', models.CharField(max_length=10)),
                ('hotel_environment', models.CharField(max_length=10)),
                ('breakfast', models.CharField(max_length=10)),
                ('lunch', models.CharField(max_length=10)),
                ('dinner', models.CharField(max_length=10)),
                ('image1', models.ImageField(upload_to=b'')),
                ('image2', models.ImageField(upload_to=b'')),
                ('image3', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='reservation_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hotel_name', models.CharField(max_length=500)),
                ('hotel_address', models.CharField(max_length=800)),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('email_address', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('cab_required', models.CharField(max_length=10)),
                ('cab_required_location', models.CharField(max_length=500)),
                ('review', models.CharField(max_length=5000)),
                ('check_in_time', models.DateTimeField()),
                ('reservation_sts', models.CharField(max_length=100)),
                ('special_reservation', models.CharField(max_length=500)),
                ('no_of_person', models.IntegerField(default=1)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cab_book_table',
            name='hotel_id',
            field=models.ForeignKey(to='GoCuisineApp.hotel_details_table'),
        ),
    ]
