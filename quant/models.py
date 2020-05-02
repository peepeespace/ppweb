from django.db import models

class Ticker(models.Model):
    code = models.CharField(max_length=10)
    company = models.CharField(max_length=100)
    market = models.CharField(max_length=10)
    sector = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)

    def __str__(self):
        return self.code