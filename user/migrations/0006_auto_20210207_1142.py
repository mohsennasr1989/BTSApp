# Generated by Django 3.1.5 on 2021-02-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210206_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]