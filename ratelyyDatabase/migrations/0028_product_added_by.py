# Generated by Django 2.1.7 on 2019-05-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0027_auto_20190429_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_by',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]