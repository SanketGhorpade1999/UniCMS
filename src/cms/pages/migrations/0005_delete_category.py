# Generated by Django 3.1.6 on 2021-03-08 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmspublications', '0008_auto_20210308_1404'),
        ('cmspages', '0004_auto_20210121_0953'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]