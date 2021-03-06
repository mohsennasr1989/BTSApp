# Generated by Django 3.1.5 on 2021-02-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210207_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='firebase_token',
            field=models.CharField(default='', max_length=200, verbose_name='User firebase Token'),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='login_token',
            field=models.CharField(default='', max_length=200, verbose_name='User login Token'),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='rule',
            field=models.CharField(default='', max_length=100, verbose_name='User Rule'),
        ),
    ]
