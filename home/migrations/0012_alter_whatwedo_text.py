# Generated by Django 3.2.2 on 2021-05-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatwedo',
            name='text',
            field=models.TextField(default='', max_length=500),
        ),
    ]