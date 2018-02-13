# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_mgmt', '0002_auto_20180201_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='creator',
            field=models.ForeignKey(related_name=b'schools', default=32, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='owner',
            field=models.ForeignKey(related_name=b'name', to=settings.AUTH_USER_MODEL),
        ),
    ]
