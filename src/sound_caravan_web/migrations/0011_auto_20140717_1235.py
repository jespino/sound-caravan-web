# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sound_caravan_web', '0010_auto_20140717_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ForeignKey(blank=True, verbose_name='Image', to='sound_caravan_web.Image', null=True),
        ),
    ]
