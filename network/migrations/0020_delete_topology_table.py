# Generated by Django 3.2.2 on 2021-06-30 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_topology_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='topology_table',
        ),
    ]
