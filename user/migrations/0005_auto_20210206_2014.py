# Generated by Django 3.1.5 on 2021-02-06 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210206_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusermodel',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='customusermodel',
            name='last_login_date',
        ),
    ]
