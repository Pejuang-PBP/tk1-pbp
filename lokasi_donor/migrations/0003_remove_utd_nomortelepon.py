# Generated by Django 3.2.7 on 2021-12-24 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lokasi_donor', '0002_auto_20211026_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utd',
            name='nomorTelepon',
        ),
    ]
