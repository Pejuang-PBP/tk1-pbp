# Generated by Django 3.2.7 on 2021-11-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_pencari_donor', '0003_alter_request_pencari_donor_nomor_induk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_pencari_donor',
            name='urgency',
            field=models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=10),
        ),
    ]
