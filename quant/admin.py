from django.contrib import admin

from quant.models import Ticker, MonitorStock, MinOHLCV

admin.site.register(Ticker)
admin.site.register(MonitorStock)
admin.site.register(MinOHLCV)