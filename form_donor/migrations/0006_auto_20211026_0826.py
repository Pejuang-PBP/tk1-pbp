# Generated by Django 3.2.7 on 2021-10-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_donor', '0005_auto_20211026_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendonor',
            name='alamat',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pendonor',
            name='komorbid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pendonor',
            name='nama_lengkap',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pendonor',
            name='nik',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pendonor',
            name='tempat_lahir',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pendonor',
            name='tinggi_badan',
            field=models.IntegerField(),
        ),
    ]