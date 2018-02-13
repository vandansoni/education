# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_1', models.CharField(max_length=50)),
                ('street_2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=10, choices=[(b'india', b'India'), (b'us', b'UnitedState'), (b'austrelia', b'Austrelia'), (b'pakistan', b'Pakistan'), (b'africa', b'Africa')])),
                ('zipcode', models.IntegerField(max_length=20)),
                ('mobile', models.IntegerField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('Logo', models.ImageField(upload_to=b'logo_images/')),
                ('website', models.CharField(max_length=200, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(related_name=b'owner_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SMARTNumber', models.CharField(max_length=20, null=True, blank=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('roll_number', models.IntegerField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.ManyToManyField(to='school_mgmt.Address')),
                ('school', models.ForeignKey(related_name=b'school_name', to='school_mgmt.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('Logo', models.ImageField(upload_to=b'logo_images/')),
                ('website', models.CharField(max_length=200, null=True, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='school',
            name='university',
            field=models.ForeignKey(related_name=b'school', to='school_mgmt.University'),
            preserve_default=True,
        ),
    ]
