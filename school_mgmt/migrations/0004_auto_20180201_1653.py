# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('school_mgmt', '0003_auto_20180201_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='creator',
        ),
        migrations.AlterField(
            model_name='school',
            name='owner',
            field=models.ForeignKey(related_name=b'schools', to=settings.AUTH_USER_MODEL),
        ),
    ]
