# Generated by Django 3.2.2 on 2021-07-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0022_auto_20210630_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='traffic_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('interface_out_1', models.CharField(max_length=50)),
                ('interface_out_2', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Traffic Interface',
                'verbose_name_plural': 'Traffic Interface',
                'ordering': ('id',),
            },
        ),
    ]
