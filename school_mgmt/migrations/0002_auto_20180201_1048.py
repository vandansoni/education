# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Address'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'University', 'verbose_name_plural': 'Universities'},
        ),
    ]
