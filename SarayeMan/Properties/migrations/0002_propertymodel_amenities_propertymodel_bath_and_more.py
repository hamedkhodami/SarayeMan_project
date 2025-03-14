# Generated by Django 5.1.1 on 2024-09-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertymodel',
            name='amenities',
            field=models.TextField(blank=True, verbose_name='امکانات'),
        ),
        migrations.AddField(
            model_name='propertymodel',
            name='bath',
            field=models.IntegerField(default=0, verbose_name='تعداد حمام'),
        ),
        migrations.AddField(
            model_name='propertymodel',
            name='beds',
            field=models.IntegerField(default=0, verbose_name='تعداد اتاق خواب'),
        ),
        migrations.AddField(
            model_name='propertymodel',
            name='garage',
            field=models.IntegerField(default=0, verbose_name='تعداد گاراژ'),
        ),
    ]
