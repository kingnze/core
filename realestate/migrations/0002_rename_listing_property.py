# Generated by Django 4.1.5 on 2023-01-04 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listing',
            new_name='Property',
        ),
    ]
