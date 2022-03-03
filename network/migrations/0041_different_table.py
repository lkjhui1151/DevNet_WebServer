# Generated by Django 3.2.2 on 2021-08-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0040_load_balance_stp_table_root_bridge'),
    ]

    operations = [
        migrations.CreateModel(
            name='different_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('different', models.CharField(blank=True, max_length=50, null=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Different LB',
                'verbose_name_plural': 'Different LB',
                'ordering': ('id',),
            },
        ),
    ]