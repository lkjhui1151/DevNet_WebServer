# Generated by Django 3.2.2 on 2021-07-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0039_auto_20210715_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='load_balance_stp_table',
            name='root_bridge',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
