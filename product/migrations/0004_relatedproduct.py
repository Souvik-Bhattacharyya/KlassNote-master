# Generated by Django 3.2.2 on 2021-05-09 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210509_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_prod', related_query_name='rel_prod', to='product.product')),
            ],
        ),
    ]
