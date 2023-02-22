# Generated by Django 4.1.5 on 2023-01-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_contact_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='property',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='property_id',
        ),
        migrations.AddField(
            model_name='contact',
            name='myproperty',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='myproperty_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]