# Generated by Django 3.2.2 on 2021-05-08 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210507_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='contact',
        ),
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
