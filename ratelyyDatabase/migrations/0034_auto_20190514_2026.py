# Generated by Django 2.1.7 on 2019-05-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0033_auto_20190514_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='scanned_counter',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
