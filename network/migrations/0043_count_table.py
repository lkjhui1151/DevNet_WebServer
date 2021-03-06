# Generated by Django 3.2.2 on 2021-08-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0042_different_table_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='count_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('switch', models.IntegerField(blank=True, max_length=50, null=True)),
                ('count', models.IntegerField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Count LB',
                'verbose_name_plural': 'Count LB',
                'ordering': ('id',),
            },
        ),
    ]
