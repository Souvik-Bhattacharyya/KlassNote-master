# Generated by Django 3.2.2 on 2021-05-08 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210508_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('intro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=1000)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.service')),
            ],
        ),
    ]
