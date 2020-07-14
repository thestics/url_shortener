from django.db import models


class Urls(models.Model):

    short = models.CharField(name='short',
                             verbose_name='Short url',
                             max_length=6)
    long = models.CharField(name='long',
                            verbose_name='Target url',
                            max_length=2048)
    expire_date = models.DateTimeField(name='expire_date')
