# Generated by Django 3.2.2 on 2021-05-20 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group_vlan_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='interface_type_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_type', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='iot_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(max_length=50, null=True)),
                ('topic', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='network_type_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_type', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='profile_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=50, null=True)),
                ('domain_lookup', models.BooleanField(default=False)),
                ('service_pwd', models.BooleanField(default=False)),
                ('domain_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='room_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='username_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='vlan_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlan_number', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('group_vlan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.group_vlan_table')),
            ],
        ),
        migrations.CreateModel(
            name='tudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=50, null=True)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(auto_now=True, null=True)),
                ('iot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.iot_table')),
            ],
        ),
        migrations.CreateModel(
            name='network_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, null=True)),
                ('pid', models.CharField(max_length=50, null=True)),
                ('sn', models.CharField(max_length=50, null=True)),
                ('interface_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.interface_type_table')),
                ('network_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.network_type_table')),
            ],
        ),
        migrations.CreateModel(
            name='match_vlan_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.profile_table')),
                ('vlan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.vlan_table')),
            ],
        ),
        migrations.AddField(
            model_name='iot_table',
            name='network',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.network_table'),
        ),
        migrations.AddField(
            model_name='iot_table',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.profile_table'),
        ),
        migrations.AddField(
            model_name='iot_table',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.room_table'),
        ),
        migrations.CreateModel(
            name='interface_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface', models.CharField(max_length=50, null=True)),
                ('interface_number', models.CharField(max_length=50, null=True)),
                ('network', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.network_table')),
            ],
        ),
    ]
