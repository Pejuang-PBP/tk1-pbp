# Generated by Django 3.2.7 on 2021-12-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tanya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pertanyaan', models.TextField()),
                ('jawaban', models.TextField()),
            ],
        ),
    ]
