# Generated by Django 2.1.7 on 2019-02-27 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('logo', models.URLField()),
                ('wiki', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'brands',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('logo', models.URLField()),
                ('wiki', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'db_table': 'companies',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Concern',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='Concern Name')),
                ('logo', models.URLField()),
                ('wiki', models.URLField()),
                ('rating', models.CharField(choices=[('0', 'Neutral'), ('1', 'Ethical'), ('2', 'Unethical')], default=0, max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'concerns',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('logo', models.URLField()),
                ('wiki', models.URLField()),
                ('gtin', models.PositiveIntegerField(verbose_name='GTIN')),
                ('image', models.URLField()),
                ('group', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratelyyDatabase.Brand')),
                ('concern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ratelyyDatabase.Concern')),
                ('concern_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_rating', to='ratelyyDatabase.Concern')),
            ],
            options={
                'db_table': 'products',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='company',
            name='concern',
            field=models.ForeignKey(db_column='concern', on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='ratelyyDatabase.Concern'),
        ),
        migrations.AddField(
            model_name='company',
            name='concern_rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies_rating', to='ratelyyDatabase.Concern'),
        ),
        migrations.AddField(
            model_name='brand',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratelyyDatabase.Company'),
        ),
        migrations.AddField(
            model_name='brand',
            name='concern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratelyyDatabase.Concern'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('id', 'brand')},
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('id', 'concern')},
        ),
    ]