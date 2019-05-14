# Generated by Django 2.1.7 on 2019-05-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratelyyDatabase', '0034_auto_20190514_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('wiki', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ManyToManyField(to='ratelyyDatabase.Product')),
            ],
            options={
                'db_table': 'certificates',
                'ordering': ('name', 'id'),
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='OrganicCertification',
        ),
    ]