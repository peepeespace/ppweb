from django.urls import path

from quant.views import (
    index,
    detail,
    TickerList,
    TickerDetail,
    StockInfoAPIView,
    IndexAPIView,
    ETFAPIView,
    OHLCVAPIView,
    BuySellAPIView,
    MarketCapitalAPIView,
    FactorAPIView,
    MonitorStockList,
    MonitorStockDetails,
    MinOHLCVList,
    UserStateList,
    UserStateDetails,
    PortHistoryList,
    PortHistoryDetails,
)


from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('ticker/', TickerList.as_view()),
    path('ticker/<int:pk>/', TickerDetail.as_view()),
    path('info/', StockInfoAPIView.as_view()),
    path('index/', IndexAPIView.as_view()),
    path('etf/', ETFAPIView.as_view()),
    path('ohlcv/', OHLCVAPIView.as_view()),
    path('buysell/', BuySellAPIView.as_view()),
    path('mktcap/', MarketCapitalAPIView.as_view()),
    path('factor/', FactorAPIView.as_view()),
    path('monitorstock/', MonitorStockList.as_view()),
    path('monitorstock/<int:pk>/', MonitorStockDetails.as_view()),
    path('minohlcv/', MinOHLCVList.as_view()),
    path('userstate/', UserStateList.as_view()),
    path('userstate/<int:pk>/', UserStateDetails.as_view()),
    path('porthistory/', PortHistoryList.as_view()),
    path('porthistory/<int:pk>/', PortHistoryDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)