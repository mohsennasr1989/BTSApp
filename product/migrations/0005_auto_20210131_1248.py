# Generated by Django 3.1.5 on 2021-01-31 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210131_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricecurrency',
            name='name',
            field=models.CharField(default='IRR', max_length=20, verbose_name='Currency Name'),
        ),
    ]