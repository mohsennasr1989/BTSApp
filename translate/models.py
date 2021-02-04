from django.db import models


# Create your models here.

class Dictionary(models.Model):
    class Meta:
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionary'
        ordering = ['id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate', 'create_date']

    def __str__(self):
        return self.item_name

    item_name = models.TextField(blank=False, default='Item', verbose_name='Item Name')
    fa_translate = models.TextField(blank=False, default='FA', verbose_name='Persian Translate')
    en_translate = models.TextField(blank=False, default='EN', verbose_name='English Translate')
    ar_translate = models.TextField(blank=False, default='AR', verbose_name='Arabic Translate')
    ru_translate = models.TextField(blank=False, default='RU', verbose_name='Russian Translate')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Create DateTime')
