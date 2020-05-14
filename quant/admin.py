from django.contrib import admin

from quant.models import Ticker, MonitorStock, MinOHLCV, UserState, PortHistory

admin.site.register(Ticker)
admin.site.register(MonitorStock)
admin.site.register(MinOHLCV)
admin.site.register(UserState)
admin.site.register(PortHistory)