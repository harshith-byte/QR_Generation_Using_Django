# Generated by Django 3.2.12 on 2022-03-23 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_name',
            name='image',
            field=models.ImageField(blank=True, upload_to='qrcode'),
        ),
    ]
