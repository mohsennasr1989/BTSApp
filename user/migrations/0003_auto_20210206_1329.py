# Generated by Django 3.1.5 on 2021-02-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210206_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusermodel',
            name='mobile',
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='Mobile Number'),
        ),
    ]