from django.contrib import admin

from quant.models import (
    Ticker,
    StockInfo,
    Index,
    ETF,
    OHLCV,
    BuySell,
    MarketCapital,
    Factor,
    MonitorStock,
    MinOHLCV,
    UserState,
    PortHistory,
)

admin.site.register(Ticker)
admin.site.register(StockInfo)
admin.site.register(Index)
admin.site.register(ETF)
admin.site.register(OHLCV)
admin.site.register(BuySell)
admin.site.register(MarketCapital)
admin.site.register(Factor)
admin.site.register(MonitorStock)
admin.site.register(MinOHLCV)
admin.site.register(UserState)
admin.site.register(PortHistory)