# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_budgetexpenses_budgetincome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgetexpenses',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='budgetincome',
            options={'ordering': ['-date']},
        ),
    ]
