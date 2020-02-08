from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title
