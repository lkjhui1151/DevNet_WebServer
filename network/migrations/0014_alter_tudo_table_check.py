# Generated by Django 3.2.2 on 2021-06-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_alter_tudo_table_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tudo_table',
            name='check',
            field=models.CharField(max_length=50),
        ),
    ]
