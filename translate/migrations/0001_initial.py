# Generated by Django 3.1.5 on 2021-01-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DictionaryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField(unique=True, verbose_name='Item Name')),
                ('fa_translate', models.TextField(default='FA', verbose_name='Persian Translate')),
                ('en_translate', models.TextField(default='EN', verbose_name='English Translate')),
                ('ar_translate', models.TextField(default='AR', verbose_name='Arabic Translate')),
                ('ru_translate', models.TextField(default='RU', verbose_name='Russian Translate')),
            ],
            options={
                'verbose_name': 'Dictionary',
                'verbose_name_plural': 'Dictionary',
                'ordering': ['id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate'],
            },
        ),
    ]