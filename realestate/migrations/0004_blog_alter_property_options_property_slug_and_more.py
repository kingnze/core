# Generated by Django 4.1.5 on 2023-01-05 23:39

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_remove_realtor_photo_realtor_realtorphoto'),
        ('realestate', '0003_property_rentorbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 1, 6, 0, 39, 25, 422500))),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'db_table': 'Blog',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'managed': True, 'verbose_name': 'Property', 'verbose_name_plural': 'Property'},
        ),
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, max_length=550, null=True),
        ),
        migrations.AlterModelTable(
            name='property',
            table='Property',
        ),
        migrations.CreateModel(
            name='Topproperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyid', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('RentOrBuy', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('photo_main', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_8', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_9', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
            options={
                'verbose_name': 'Topproperty',
                'verbose_name_plural': 'Topproperty',
                'db_table': 'Topproperty',
                'managed': True,
            },
        ),
    ]
