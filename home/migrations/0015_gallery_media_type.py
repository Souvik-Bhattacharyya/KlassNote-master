# Generated by Django 3.2.2 on 2021-05-11 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210510_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='media_type',
            field=models.CharField(choices=[('0', 'Image'), ('1', 'Video')], default='0', max_length=1),
        ),
    ]