# Generated by Django 3.2.2 on 2021-05-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_gallery_media_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.FileField(upload_to='gallery/'),
        ),
    ]
