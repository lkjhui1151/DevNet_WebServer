# Generated by Django 3.2.2 on 2021-06-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_tudo_table_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tudo_table',
            options={'ordering': ('id',), 'verbose_name': 'Event Log', 'verbose_name_plural': 'Event Log'},
        ),
        migrations.AddField(
            model_name='tudo_table',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]
