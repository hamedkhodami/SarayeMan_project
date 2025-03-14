# Generated by Django 5.1.1 on 2024-09-28 16:11

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=200, verbose_name='نام کامل')),
                ('Phone', models.CharField(max_length=50, null=True, verbose_name='شماره تماس')),
                ('Email', models.EmailField(max_length=200, verbose_name='ایمیل')),
                ('Message', models.TextField(max_length=200, verbose_name='متن')),
                ('created_at', django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ ثبت نظر')),
            ],
            options={
                'verbose_name': 'ارتباط',
                'verbose_name_plural': 'ارتباطات',
            },
        ),
    ]
