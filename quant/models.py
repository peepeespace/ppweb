from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Ticker(models.Model):
    code = models.CharField(max_length=10)
    company = models.CharField(max_length=100)
    market = models.CharField(max_length=10)
    sector = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)

    def __str__(self):
        return self.code

class MonitorStock(models.Model):
    user = models.ForeignKey(User,
                             default=1,
                             on_delete=models.CASCADE,
                             related_name='monitorstock')
    date = models.CharField(max_length=20)
    codelist = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.user.username, self.date)

class MinOHLCV(models.Model):
    code = models.CharField(max_length=10)
    date = models.CharField(max_length=20)
    openp = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    close = models.IntegerField()
    volume = models.BigIntegerField()

    def __str__(self):
        return '{} {}'.format(self.code, self.date)