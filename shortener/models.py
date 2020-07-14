from django.db import models

from shortener.const import URL_SIZE


class Url(models.Model):

    short = models.CharField(name='short',
                             verbose_name='Short url',
                             max_length=URL_SIZE)
    long = models.CharField(name='long',
                            verbose_name='Target url',
                            max_length=2048)
    expire_date = models.DateTimeField(name='expire_date')
    used_times = models.PositiveIntegerField(default=0)
