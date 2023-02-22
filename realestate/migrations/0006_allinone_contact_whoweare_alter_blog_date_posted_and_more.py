# Generated by Django 4.1.5 on 2023-01-08 08:47

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_remove_realtor_photo_realtor_realtorphoto'),
        ('realestate', '0005_alter_property_options_alter_topproperty_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allinone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Whoweare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('property', models.CharField(max_length=500)),
                ('advice', models.CharField(max_length=500)),
                ('services', models.CharField(max_length=500)),
                ('responsibility', models.CharField(max_length=500)),
                ('structure', models.CharField(max_length=500)),
                ('strategy', models.CharField(max_length=500)),
                ('body', ckeditor.fields.RichTextField()),
                ('published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Whoweare',
                'verbose_name_plural': 'Whoweare',
                'db_table': 'Whoweare',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 8, 9, 47, 23, 188761)),
        ),
        migrations.CreateModel(
            name='Top_properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('RentOrBuy', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.CharField(blank=True, max_length=20)),
                ('bathrooms', models.CharField(blank=True, max_length=20)),
                ('garage', models.CharField(blank=True, max_length=20)),
                ('sqft', models.CharField(blank=True, max_length=20)),
                ('plot_size', models.CharField(blank=True, max_length=50)),
                ('photo_main', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('RentOrBuy', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.CharField(blank=True, max_length=20)),
                ('bathrooms', models.CharField(blank=True, max_length=20)),
                ('garage', models.CharField(blank=True, max_length=20)),
                ('sqft', models.IntegerField(blank=True)),
                ('plot_size', models.CharField(blank=True, max_length=50)),
                ('photo_main', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]
