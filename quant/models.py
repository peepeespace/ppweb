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

class UserState(models.Model):
    user = models.ForeignKey(User,
                             default=1,
                             on_delete=models.CASCADE,
                             related_name='state')
    date = models.CharField(max_length=20)
    want_state = models.CharField(max_length=10) # 1: on, 0: off
    tool_state = models.CharField(max_length=10) # 1: on, 0: off, 2: turning on, 3: turning off
    port_state = models.CharField(max_length=10) # 1: stock bought, 0: no stocks bought

    def __str__(self):
        return self.user.username

class PortHistory(models.Model):
    user = models.ForeignKey(User,
                             default=1,
                             on_delete=models.CASCADE,
                             related_name='history')
    date = models.CharField(max_length=20)
    traded_stock = models.CharField(max_length=20)
    traded_time = models.CharField(max_length=20)
    action = models.CharField(max_length=10) # 1: buy, 0: sell
    amount = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.user.username
    