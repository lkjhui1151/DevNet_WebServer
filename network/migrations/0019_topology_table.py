# Generated by Django 3.2.2 on 2021-06-30 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0018_delete_topology_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='topology_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface', models.ManyToManyField(to='network.interface_table')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.iot_table')),
                ('vlan', models.ManyToManyField(to='network.vlan_table')),
            ],
            options={
                'verbose_name': 'Topology',
                'verbose_name_plural': 'Topology',
                'ordering': ('id',),
            },
        ),
    ]
